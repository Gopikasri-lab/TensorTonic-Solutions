import numpy as np

def ridge_regression(X, y, lr, epochs, alpha):
    X = np.array(X, dtype=np.float64)
    y = np.array(y, dtype=np.float64)
    n, d = X.shape
    w = np.zeros(d, dtype=np.float64)
    b = 0.0

    for i in range(epochs):
        y_hat = X @ w + b
        error = y_hat - y
        grad = X.T @ error          # compute base gradient first
        dw = (2/n) * grad + 2 * alpha * w
        db = (2/n) * np.sum(error)
        w = w - lr * dw
        b = b - lr * db

    weights = [round(x, 4) for x in w.tolist()]
    bias = round(float(b), 4)

    return weights, bias