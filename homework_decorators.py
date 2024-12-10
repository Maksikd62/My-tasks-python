import time
#decorators (exercise1)
def all_time(func):
    def difference():
        start_time=time.time()
        result=func()
        end_time=time.time()
        difference_time=end_time-start_time
        return difference_time, result
    return difference

@all_time
def numbers():
    even_numbers=[]
    for num in range(1, 100000):
        if num%2==0:
            even_numbers.append(num)
    return even_numbers

time_for_func, even_numbers = numbers()
print(even_numbers)
print("Time for function: "+ str(time_for_func))

#decorators (exercise2)
def fix_params(func):
    def wrapper(args):
        new_args = []
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                new_args.append(abs(arg))
            else:
                new_args.append(arg)
        return func(new_args)
    return wrapper

@fix_params
def example_func(args):
    return args

print(example_func([10, -3, "red", -1, 200, -5, 2]))