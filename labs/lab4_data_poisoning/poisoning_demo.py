import argparse, numpy as np, pandas as pd
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import random

DATA_CSV = "../../datasets/synthetic_poison_demo.csv"

def flip_labels(y, rate):
    y_poison = y.copy()
    n = int(len(y) * rate)
    idx = np.random.choice(len(y), n, replace=False)
    classes = np.unique(y)
    for i in idx:
        others = [c for c in classes if c != y_poison[i]]
        y_poison[i] = random.choice(others)
    return y_poison, idx

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--poison", type=float, default=0.1)
    ap.add_argument("--contamination", type=float, default=0.1)
    args = ap.parse_args()

    df = pd.read_csv(DATA_CSV)
    X = df[[c for c in df.columns if c.startswith("f")]].values
    y = df["label"].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    clf_clean = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_train, y_train)
    acc_clean = accuracy_score(y_test, clf_clean.predict(X_test))

    y_train_poison, poisoned_idx = flip_labels(y_train, args.poison)
    clf_poison = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_train, y_train_poison)
    acc_poison = accuracy_score(y_test, clf_poison.predict(X_test))

    iso = IsolationForest(contamination=args.contamination, random_state=42).fit(X_train)
    flags = iso.predict(X_train)
    keep = flags == 1

    clf_cleaned = RandomForestClassifier(n_estimators=200, random_state=42).fit(X_train[keep], y_train_poison[keep])
    acc_cleaned = accuracy_score(y_test, clf_cleaned.predict(X_test))

    print(f"Clean accuracy:    {acc_clean:.3f}")
    print(f"Poisoned accuracy: {acc_poison:.3f} (poison rate={args.poison})")
    print(f"Cleaned accuracy:  {acc_cleaned:.3f} (removed {(~keep).sum()} suspected samples)")
