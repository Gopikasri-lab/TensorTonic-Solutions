import torch

def reshape_tensor(x, op):
    """
    Returns: list
    """
    x= torch.tensor(x,dtype = torch.float32)
    if op =="flatten":
        p=x.flatten()
    elif op == "squeeze":
        p=x.squeeze()
    else:
        p = x.T

    return p.tolist()
    pass
