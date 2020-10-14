import numpy as np 

def MoM(x,k):
    '''
    MoM estimator with data x.
    k is the number of groups. 
    '''
    means = []
    try: 
        for y in np.split(x,k):
            means.append(y.mean())
        return np.median(means)
    except: 
        return 'Cant split with that k :('