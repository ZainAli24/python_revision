# ▼Problem 2: Debugging Function Calls
# Problem: Create a decorator to print the function name and the values of its arguments every time the function is called.


def decorator(func):
    def wrapper(*args, **kwargs):
        args_values = ', '.join(str(arg) for arg in args)
        kwargs_values = ', '.join(f"{key}: {value}" for key, value in kwargs.items())
        print(f"Function name is {func.__name__} calling with its args {args_values} and kwargs {kwargs_values}")
        result = func(*args, **kwargs)
        return result
    return wrapper




@decorator
def greet(name, greeting="Hanji"):
    print(f"{greeting}, {name}")

greet("ZAIN", greeting="Asslam-o-Alikum")



@decorator
def example_function(*args, **kwargs):
    sumis = sum(args)
    key_values = ', '.join((f'{k}: {v}' for k, v in kwargs.items()))
    print(f"Sum is {sumis} and key, values is {key_values}")

example_function(5, 10, 15, name= "ZAIN", age= "20")
