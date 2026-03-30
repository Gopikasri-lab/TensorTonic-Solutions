import numpy as np
def promote_model(models):
    """
    Decide which model version to promote to production"""
    model = max(models,key = lambda x:(x['accuracy'],-x['latency'],x['timestamp']))
    return model['name']
    
    
    
    pass