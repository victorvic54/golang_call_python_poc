# foo.py
import time

def hello():
    """
    Print hello world for fun and profit.
    """
    print("Hello, world! This function will panic soon!")
    raise Exception("Help")
    # try:
    #     raise Exception("Help")
    # except Exception as ex:
    #     print("Error thrown: %s" % ex)
    #     raise Exception ("Re-raise error")

    print("Done panicking")
    
    return "Hi from foo.py"