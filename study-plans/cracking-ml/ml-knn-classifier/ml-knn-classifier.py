import numpy as np

def knn_classify(X_train, y_train, X_test, k=3):
    """
    Returns: A list of predicted integer labels for each test point
    """
    X_train = np.array(X_train)
    n,d = X_train.shape
    y_train = np.array(y_train)
    X_test = np.array(X_test)
    output = []
    for x in X_test:
        dist = np.sqrt(np.sum((X_train - x)**2,axis = 1))
        nn = np.argsort(dist)[:k]
        nn1 = y_train[nn]
        count = np.bincount(nn1)
        output.append(np.argmax(count))
        

    return output
        
        
    
            
            
    
    
    pass
