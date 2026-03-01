import numpy as np

def _sigmoid(z):
    """Numerically stable sigmoid implementation."""
    return np.where(z >= 0, 1/(1+np.exp(-z)), np.exp(z)/(1+np.exp(z)))

def train_logistic_regression(X, y, lr=0.1, steps=1000):
    """
    Train logistic regression via gradiwt descent.
    Return (w, b).
    """
    n_data,n_features = X.shape
    w = np.zeros(n_features)
    b = 0.0

    for _ in range(steps):
        Z = X@w+b
        p = _sigmoid(Z)
        w = w - ((lr*(X.T@(p-y)))/n_data)
        b = b - ((lr*np.sum(p-y))/n_data)

    return (w,b)
        
        
    