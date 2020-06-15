import numpy as np

def get_new_numpy_array():
    print("I was called from bar, returning a new numpy_array")
    return np.array([11, 22, 33])

class Person():
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print("My name is %s %s" % (self.firstname, self.lastname))