import numpy as np

def find_near(array,value):

    """
    insert an array you're looking for a value near
    and the value you're looking for
    outputs teh index of that array value as well
    as the value itself
    """
    idx = (np.abs(array-value)).argmin()
    return (idx,array[idx])
