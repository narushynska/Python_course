from time import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print 'Execution time of function {function}: {time}'.format(function = str(func.__name__), time =(end - start)*100)
        return result
    return wrapper
