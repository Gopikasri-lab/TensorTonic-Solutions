import numpy as np

def linear_regression(X, y, lr, epochs):
    X = np.array(X)
    y = np.array(y)
    n,d = X.shape
    w= np.zeros(d)
    b=0.0
    for i in range(epochs):
        y_hat = X@w +b
        dw = (2.0/n) * X.T @(y_hat - y)
        db = (2/n)*np.sum(y_hat-y)
        w = w-(dw*lr)
        b = b-(db*lr)
    return (w,b)
    """
    Returns: tuple (weights, bias)
    """
    pass
