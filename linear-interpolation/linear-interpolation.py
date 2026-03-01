def linear_interpolation(values):
    """
    Fill missing (None) values using linear interpolation.
    """
    for i in range(0,len(values)):
        if values[i] != None:
            vleft = values[i]
            left = i
        else:
            for j in range(i+1,len(values)):
                if values[j] !=None:
                    vright = values[j]
                    right = j
                    break
                    
                    
            values[i] = vleft +(((i-left)/(right -left))*(vright-vleft))
    return values
                                

                                
            
        
        
    
    