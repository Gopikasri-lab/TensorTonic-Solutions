import numpy as np
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    points = np.array(points)
    assignments = np.array(assignments)
    centroid = []
    c= np.zeros((k,points.shape[1]))

    for i in range(k):
        centre = points[assignments==i]

        if len(centre)>0:
            centroid.append((np.mean(centre, axis= 0)).tolist())
        else:
            centroid.append((np.zeros(points.shape[1])).tolist())

    return centroid
            
        
    
    # Write code here