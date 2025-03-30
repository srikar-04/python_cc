# create a decorator to print the function name and the values of it's arguments everytime the function is called

def func_details(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        function_arguments = [args, kwargs]
        print(f'function name and arguments are {function_name}, {function_arguments}')
        return [function_name, function_arguments]
    return wrapper

@func_details
def example_func(num_1, num_2):
    print(f'this function arguments are, {num_1, num_2}')

example_func(2, 5)