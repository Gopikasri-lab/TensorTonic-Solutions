import numpy as np
from collections import Counter
import statistics

# Returns the single most common element

def mean_median_mode(x):
    """
    Returns: dict with 'mean', 'median', 'mode' as floats.
    """
    if len(x)<=0:
        return
    else:
        mean = np.mean(x)
        median = np.median(x)
        freq = Counter(x)
        max_freq = max(freq.values())
        #mode = max(set(x), key=list(x).count)
        mode = statistics.mode(x)
        # mode = item  (for item,count in freq.items() if count == max_freq)
        # mode = 1.0
        d = {"mean":float(mean),
            "median":float(median),
            "mode":float(mode)}
        return d
    