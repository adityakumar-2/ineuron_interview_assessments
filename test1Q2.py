from functools import wraps
import time
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def timer(func):
    @wraps(func)
    def wrapper(a):
        start_time = time.time();
        result = func(a)
        print("the function ends in ", time.time()-start_time, "secs")
        return result
    return wrapper
    
@timer
def only_even(x):
    return [a for a in x if a%2 == 0]

print(only_even(a))