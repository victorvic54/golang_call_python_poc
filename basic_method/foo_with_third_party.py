# foo.py
import time
import numpy as np

def hello():
    """
    Print hello world for fun and profit.
    """
    numpy_arr = np.array([1, 2, 3])

    print("Hello, world! It is %s" % time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()))
    print("Numpy shape of %s : %s" % (numpy_arr, numpy_arr.shape))

    return numpy_arr