# create a decorator to print the function name and the values of it's arguments everytime the function is called

def func_details(func):
    def wrapper(*args, **kwargs):
        function_name = func.__name__
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ', '.join(f'{k}:{v}' for k, v in kwargs.items())
        # print(f'function name and arguments are {function_name} and {function_arguments}')
        print(f'arguments are {args_value} and kw_arguments are {kwargs_value}')
        return func(*args, **kwargs)
    return wrapper

@func_details
def example_func(num_1, num_2):
    print('Hello from example function')

example_func(2, 5)