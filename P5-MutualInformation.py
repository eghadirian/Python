import numpy as np

def mutual_information(arr):
    return  entropy(arr) \
            - entropy(np.sum(arr, axis = 0)) \
            - entropy(np.sum(arr, axis = 1))
def entropy(x):
    return np.sum(x*np.log(x), where = x > 0) or 0