import torch

def create_tensor(method, shape, value=0.0):
    """
    Returns: list
    
    
    """
    try: 
            shape = tuple(shape)
            if method == "ones":
                p=torch.ones(shape)
            elif method == "zeros":
                p=torch.zeros(shape)
            else:
                p=torch.full(shape,value)
    except IndexError as ie:
        
        print(IndexError)

    return p.tolist()
    pass