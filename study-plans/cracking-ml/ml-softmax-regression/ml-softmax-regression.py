import numpy as np

def softmax_regression(X, y, n_classes, lr=0.01, n_iters=1000):
    """
    Returns: tuple (weights, bias) where weights is a 2D list (d x K) and bias is a list of length K
    """
    X = np.array(X,dtype = np.float64)
    y = np.array(y)
    
    
    n,d = X.shape
    Y = np.zeros((n,n_classes))
    Y[np.arange(n),y] = 1
    w = np.zeros((d,n_classes))
    b= np.zeros((1,n_classes))
    
    for i in range(n_iters):
        Z = X@w+b
        expz = np.exp(Z)
        P = expz/(np.sum(expz,axis = 1, keepdims = True))
        grad = X.T@(P-Y)
        dw = (1/n)*grad
        db = (1/n)*np.sum((P-Y), axis=0,keepdims = True)
        w = w-lr*dw
        b = b- lr*db

    return w,b[0]
        
    
    
    pass
