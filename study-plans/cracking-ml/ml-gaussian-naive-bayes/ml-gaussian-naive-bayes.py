import numpy as np

def gaussian_nb(X_train, y_train, X_test):
    """
    Returns: A list of predicted integer labels for each test point
    """
    X_train = np.asarray(X_train,dtype = float)
    y_train = np.asarray(y_train,dtype = int)
    classes = np.unique(y_train)
    n= len(y_train)
    stats = {}
    e = 1e-9
    for c in classes:
        m = y_train==c
        val = X_train[m]
        stats[c]={
            'prior': np.log(len(m)/n),
            'mean' : np.mean(val, axis=0),
            'var' : np.var(val,axis=0) + e 
        }
    X_test = np.asarray(X_test,dtype = float)
    predictions = []
    for x in X_test:
        best_value = -np.inf
        best_class = None
        for c in classes:
            s = stats[c]

            logpc = s['prior']
            logpc+=np.sum((-0.5*np.log(2*np.pi*s['var'])) - (((x-s['mean'])**2)/(2*s['var'])))
            if logpc > best_value:
                best_value = logpc
                best_class = c
        predictions.append(int(best_class))

    return predictions
            
        
    pass
