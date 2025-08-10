import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

app = FastAPI(title="Vulnerable Iris Classifier API")

class Inp(BaseModel):
    x: list

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42).fit(X_train, y_train)

@app.post("/predict")
def predict(inp: Inp):
    arr = np.array(inp.x, dtype=float).reshape(1,-1)
    proba = model.predict_proba(arr)[0].tolist()
    label = int(np.argmax(proba))
    return {"label": label, "proba": proba}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
