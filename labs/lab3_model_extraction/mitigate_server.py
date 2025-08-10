import uvicorn, time
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from collections import defaultdict
import argparse

app = FastAPI(title="Mitigated Iris Classifier API")

class Inp(BaseModel):
    x: list

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train, y_train)

RATE_BUCKET = defaultdict(list)

def rate_limit(ip: str, limit: int):
    now = time.time(); window = 10
    RATE_BUCKET[ip] = [t for t in RATE_BUCKET[ip] if now - t < window]
    if len(RATE_BUCKET[ip]) >= limit: return False
    RATE_BUCKET[ip].append(now); return True

@app.post("/predict")
def predict(inp: Inp, x_api_key: str = Header(None), x_forwarded_for: str | None = Header(None)):
    if x_api_key != app.state.api_key:
        raise HTTPException(status_code=401, detail="Invalid API key")
    ip = x_forwarded_for or "local"
    if not rate_limit(ip, app.state.rate):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    arr = np.array(inp.x, dtype=float).reshape(1,-1)
    label = int(model.predict(arr)[0])
    return {"label": label}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--api-key", default="SECRET123")
    parser.add_argument("--rate", type=int, default=5)
    args = parser.parse_args()
    app.state.api_key = args.api_key
    app.state.rate = args.rate
    uvicorn.run(app, host="127.0.0.1", port=8000)
