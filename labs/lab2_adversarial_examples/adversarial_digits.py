import argparse, numpy as np, pandas as pd
import matplotlib.pyplot as plt

DIGITS_CSV = "../../datasets/digits.csv"

def softmax(z):
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)

def one_hot(y, K):
    Y = np.zeros((y.shape[0], K), dtype=np.float64)
    Y[np.arange(y.shape[0]), y] = 1.0
    return Y

def train_softmax(X, y, lr=0.5, epochs=300, reg=1e-4):
    n, d = X.shape
    K = int(y.max()) + 1
    W = np.zeros((d, K)); b = np.zeros((1, K))
    Y = one_hot(y, K)
    for _ in range(epochs):
        logits = X @ W + b
        P = softmax(logits)
        dlogits = (P - Y) / n
        dW = X.T @ dlogits + reg * W
        db = dlogits.sum(axis=0, keepdims=True)
        W -= lr * dW; b -= lr * db
    return W, b

def predict(W, b, X): return np.argmax(X @ W + b, axis=1)

def fgsm(W, b, x, y_true, epsilon):
    logits = x @ W + b
    p = softmax(logits)
    K = p.shape[1]
    y1 = np.zeros((1, K)); y1[0, y_true] = 1.0
    grad_logits = (p - y1)
    grad_x = grad_logits @ W.T
    x_adv = x + epsilon * np.sign(grad_x)
    return np.clip(x_adv, 0.0, 1.0)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--epsilon", type=float, default=0.5)
    args = ap.parse_args()

    df = pd.read_csv(DIGITS_CSV)
    X = df[[c for c in df.columns if c.startswith("p")]].values.astype(np.float64) / 16.0
    y = df["label"].values.astype(int)

    n = X.shape[0]; idx = np.arange(n)
    np.random.seed(42); np.random.shuffle(idx)
    split = int(0.8*n); tr, te = idx[:split], idx[split:]
    Xtr, ytr, Xte, yte = X[tr], y[tr], X[te], y[te]

    W, b = train_softmax(Xtr, ytr)

    for i in range(len(Xte)):
        x = Xte[i:i+1]; ytrue = yte[i]
        ypred = predict(W, b, x)[0]
        if ypred == ytrue:
            x_adv = fgsm(W, b, x, ytrue, args.epsilon)
            y_adv = predict(W, b, x_adv)[0]
            fig = plt.figure()
            plt.suptitle(f"FGSM eps={args.epsilon} | true={ytrue} pred={ypred} -> adv_pred={y_adv}")
            plt.subplot(1,2,1); plt.imshow((x*16.0).reshape(8,8), cmap="gray"); plt.axis("off"); plt.title("Original")
            plt.subplot(1,2,2); plt.imshow((x_adv*16.0).reshape(8,8), cmap="gray"); plt.axis("off"); plt.title("Adversarial")
            fig.savefig("adv_result.png", bbox_inches="tight"); print("Saved adv_result.png"); return
    print("No correctly classified sample found; rerun.")

if __name__ == "__main__": main()
