import numpy as np

def percentiles(x, q):
    """
    Returns: numpy array of percentile values.
    """
    y = [np.percentile(x,q1) for q1 in q]
    y = np.asarray(y)
    return y
    pass
