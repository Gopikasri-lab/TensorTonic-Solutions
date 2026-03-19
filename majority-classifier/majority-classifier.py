import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    # Write code here
    k=len(X_test)
    label = np.unique(y_train,return_counts = True)
    id = np.argmax(label[1])
    max_label = label[0][id]
    return np.full(k,max_label)
    
    
    pass