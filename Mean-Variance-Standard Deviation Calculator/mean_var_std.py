import numpy as np

def calculate(the_list):
    
    if len(the_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    mean =[]
    variance = []
    std_dev = []
    v_max = []
    v_min = []
    v_sum = []  
    
    arr = np.array(the_list)
    arr = arr.reshape((3,3))
    
    for i in range(2):
        
        mean.append(list(arr.mean(axis = i)))
        v_max.append(list(arr.max(axis = i)))
        v_min.append(list(arr.min(axis = i)))
        v_sum.append(list(arr.sum(axis = i)))
        std_dev.append(list(arr.std(axis = i)))
        variance.append(list(arr.var(axis = i)))
             
    mean.append(arr.mean())
    v_max.append(arr.max())
    v_min.append(arr.min())
    v_sum.append(arr.sum())
    std_dev.append(arr.std())
    variance.append(arr.var())
    
    
    
    calculations = {
        
        'mean' : mean,
        'variance' : variance,
        'standard deviation' : std_dev,
        'max' : v_max,
        'min' : v_min,
        'sum' : v_sum
        
        }

    return calculations


#print(calculate([2,6,2,8,4,0,1,5,7]))