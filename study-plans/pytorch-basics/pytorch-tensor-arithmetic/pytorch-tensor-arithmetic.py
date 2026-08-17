import torch

def tensor_op(x, y, op):
    """
    Returns: list (result tensor converted via .tolist())
    """
    x = torch.tensor(x,dtype = torch.float32)
    y = torch.tensor(y,dtype = torch.float32)
    if op == "add":
        p = torch.add(x,y)
    elif op == "multiply":
        
        p = torch.mul(x,y)
    elif op == "matmul":
        #if len(x[0])==len(y[1]):
        p = torch.matmul(x,y)
        
    elif op == "power":
        p= x**y
        
    else:
        p = torch.max(x,y)
        
    pass
    return p.tolist()