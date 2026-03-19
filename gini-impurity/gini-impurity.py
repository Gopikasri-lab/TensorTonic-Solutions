import numpy as np

def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    # Write code here
    
    
    if len(y_left)==0:
        gini_left = 0
    else:
        left_class = np.unique(y_left,return_counts=True)
        gini_left = left_class[1]/len(y_left)  
        gini_left = 1-np.sum((gini_left)**2)
        
    if len(y_right)==0:
        gini_right=0
    else:
        right_class = np.unique(y_right,return_counts = True)
        gini_right = right_class[1]/len(y_right)
        gini_right = 1 - np.sum((gini_right)**2)
        
    
    
  
    N = len(y_left)+len(y_right)
    if N == 0:
        return 0.0  # nothing to split
    gini_split = ((len(y_left)/N)*gini_left)+((len(y_right)/N)*gini_right)

    return gini_split
    pass