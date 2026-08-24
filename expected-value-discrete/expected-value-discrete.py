import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Return the expected value of the discrete distribution.
    """
    # Write code here
    x = np.asarray(x,dtype = float)
    p = np.asarray(p,dtype = float)
    exp = np.dot(x,p)
    pass
    return exp