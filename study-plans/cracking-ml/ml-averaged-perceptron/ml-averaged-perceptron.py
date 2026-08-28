import numpy as np

def averaged_perceptron(X_train, y_train, X_test, n_epochs=10):
    """
    Returns: A list of predicted labels (-1 or +1) for each test point
    """
    X_train = np.asarray(X_train, dtype = float)
    y_train = np.asarray(y_train, dtype = float)
    X_test = np.asarray(X_test, dtype = float)
    n = X_train.shape[1]
    b=0.0
    w = np.zeros(n)
    n1= X_train.shape[0]
    T = n1*n_epochs
    count = 0
    w_sum = np.zeros(n)
    b_sum = 0.0
    for epoch in range(n_epochs):
        for i in range(n1):
            if y_train[i]*(w@X_train[i] + b )<=0:
                w = w + y_train[i]*X_train[i]
                b = b+ y_train[i]
            w_sum+=w
            b_sum+=b
            count+=1
        w_avg = w_sum/count
        b_avg = b_sum/count

    predictions = []
    m = X_test.shape[0]
    for i in range(m):
        if (w_avg@X_test[i] + b_avg)>0:
            predictions.append(1)
        else:
            predictions.append(-1)
    return predictions
            
        
    
    
