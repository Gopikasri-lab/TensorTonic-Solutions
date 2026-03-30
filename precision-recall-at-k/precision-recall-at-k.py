def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    recommended = recommended[:k]
    j=0
    for i in recommended:
        if i in relevant:
            j+=1
    precision = j/k
    recall = j/len(relevant)
    return [precision,recall]
            
        
        
    # Write code here