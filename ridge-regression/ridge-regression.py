import numpy as np
def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    X = np.array(X)
    y = np.array(y)
    k = X.shape[1]
    I = lam*np.eye(k)
    w1 = np.linalg.pinv((X.T)@X + I)
    w = w1@((X.T)@y)
    return w.tolist()
    
    
    # Write code here