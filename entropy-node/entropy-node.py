import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Write code here
    if len(y)==0:
        return 0.0
    b=0
    Y = np.unique(y,return_counts=True)
    counts = Y[1]/sum(Y[1])
    for i in counts:
        if i>0:
            b= b- (i*(np.log2(i)))

    return b
    
    pass