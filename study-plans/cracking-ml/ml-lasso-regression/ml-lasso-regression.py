def lasso_regression(X, y, lr, epochs, alpha):
    """
    Perform Lasso Regression using gradient descent with L1 subgradient.
    Returns: tuple of (weights_list, bias_float)
    """

    X = np.array(X,dtype=np.float64)
    y = np.array(y,dtype=np.float64)
    n,d  = X.shape
    w = np.zeros(d,dtype=np.float64)
    b = 0.0
    for i in range(epochs):
        Y_hat = X@w + b
        error = Y_hat - y
        error_s = X.T@error
        dw = (2/n)*error_s + (alpha*np.sign(w))
        db = (2/n)*np.sum(Y_hat-y)
        w = w - lr*dw
        b= b - lr*db

    return [round(x, 4) for x in w.tolist()], round(float(b), 4)