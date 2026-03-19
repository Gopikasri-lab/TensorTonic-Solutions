import numpy as np
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    points = np.array(points)
    centroids = np.array(centroids)
    D = points.shape[0]
    best_idx = 0
    cluster = []
    
    for i in points:
        
        dist = np.sum((i-centroids)**2,axis=1)
        min = np.argmin(dist)
        cluster.append(int(min))
    return cluster
    
            
            
        