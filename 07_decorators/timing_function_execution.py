# Measuring time taken by a function to execute, using decorators

import time

def timer(func):             # timer is a higher order function which can take function as an argument and can return a function
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} ran in {end-start} time')
        return result
    return wrapper    # here we are returning another function

@timer   # the below function has to pass through this timer function only. Now this timer is a decorator
def example_func(n):
    time.sleep(n)

example_func(2)