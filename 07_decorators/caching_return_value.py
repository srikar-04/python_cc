import time

def cache(func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return cache_value[args]
    return wrapper



@cache
def long_running_func(a, b):
    time.sleep(4)
    return a + b

print(long_running_func(2, 3))
print(long_running_func(2, 3))    # this call runs immediately because the result is already in the cahced memory. If the arguments chages then the second print statement also takes 4 mins of time. for example see the below function call with different arguments
print(long_running_func(5, 5))   # this will take 4 more seconds to execute because this functions arguments addition is not present in the cache memory