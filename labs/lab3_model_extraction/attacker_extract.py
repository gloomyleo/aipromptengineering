import argparse, random, time
import numpy as np
import requests
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def random_iris_sample():
    sl = random.uniform(4.0, 8.0)
    sw = random.uniform(2.0, 4.5)
    pl = random.uniform(1.0, 7.0)
    pw = random.uniform(0.1, 2.5)
    return [sl, sw, pl, pw]

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default="http://127.0.0.1:8000/predict")
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--outfile", default="stolen.csv")
    ap.add_argument("--api-key", default=None)
    args = ap.parse_args()

    headers = {}
    if args.api_key: headers["x-api-key"] = args.api_key

    X, y = [], []
    for i in range(args.n):
        x = random_iris_sample()
        try:
            r = requests.post(args.url, json={"x": x}, headers=headers, timeout=5)
            if r.status_code == 429: time.sleep(1.0); continue
            r.raise_for_status()
            data = r.json()
            label = data.get("label", data.get("label"))
            X.append(x); y.append(label)
        except Exception as e:
            print("Request error:", e)
        if (i+1) % 100 == 0: print(f"Collected {i+1} samples")

    with open(args.outfile, "w") as f:
        for a,b in zip(X,y): f.write(",".join(map(str,a)) + f",{b}\n")
    print(f"Saved {len(X)} rows to {args.outfile}")

    X, y = np.array(X), np.array(y)
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)
    clone = DecisionTreeClassifier(random_state=42).fit(Xtr, ytr)
    acc = accuracy_score(yte, clone.predict(Xte))
    print("Clone accuracy on holdout:", acc)
