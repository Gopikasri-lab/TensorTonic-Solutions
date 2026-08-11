import math
def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    # Write code here
    a = []
    for i in values:
        theta = (2*math.pi*i)/(period)
        angle = [math.sin(theta),math.cos(theta)]
        a.append(angle)
    return a
        