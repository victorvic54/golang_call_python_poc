import time
import arrow
import threading
import buz_example
import logging
import numpy as np

def multiply_two(arr):
    for i in range(len(arr)):
        arr[i] *= 2


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(1)
    logging.info("Thread %s: finishing", name)


def hello():
    """
    Print hello world for fun and profit.
    """
    numpy_arr = np.array([1, 2, 3])

    # Import built in function
    print("Hello, world! It is %s" % time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime()))
    
    # Import third party libraries
    utc = arrow.utcnow()
    local = utc.to('US/Pacific')
    print("Arrow curr date: %s" % local.format())
    print("Numpy shape of %s : %s" % (numpy_arr, numpy_arr.shape))

    print

    # Execute python threading
    threads = list()
    for index in range(3):
        print("Main : create and start thread %d" % index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        print("Main : before joining thread %d" % index)
        thread.join()
        print("Main : thread %d done" % index)

    print

    # call from other class
    numpy_arr = buz_example.get_new_numpy_array()

    # python logging
    logging.info("Logging info wont be shown in the console output")
    logging.exception("Logging exception will be shown in the console output")

    # inheritance
    student = Student("Vic", "tor")
    student.printname()
    student.study()
    print(Student.static_var)
    print
    
    return numpy_arr


def get_new_arr(param):
    return param + buz_example.get_new_numpy_array()


class Student(buz_example.Person):
    static_var = "I am a static method"

    def study(self):
        print("%s %s is currently studying" % (self.firstname, self.lastname))
