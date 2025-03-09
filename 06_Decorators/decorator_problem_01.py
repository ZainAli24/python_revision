# ▼Problem 1: Timing Function Execution
# Problem: Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"{func.__name__} ran in {(end_time - start_time):.0f} seconds ")
        return result
    return wrapper

@timer
def example_function(n):
    time.sleep(n)
    return "My Name is ZAIN"


res = example_function(3)
print(f"Final result: {res}")


#--------------------------------------------------------------------------------------------------
# internal working of upper decorator function:
def timer1(func):
    def wrapper1(*args, **kwargs):
        print("THis is wrapper")
        result1 = func(*args, **kwargs)
        return result1
    return wrapper1

example_function1 = timer1(example_function1)
example_function1 = wrapper1   # timer return wrapper function
example_function1(3) = wrapper(3)
