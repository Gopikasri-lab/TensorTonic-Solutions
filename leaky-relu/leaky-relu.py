import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    X1=[]
    for i in x:
        if i>=0:
            X1.append(i)
        else:
            X1.append(alpha*i)
    
    X1 = np.array(X1)
    return X1