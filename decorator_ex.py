# decorator
def my_decorator(func):  # function as a parameter
    def func_wrapper(*args, **kwargs):
        print("Before calling " + func.__name__)
        result = func(*args, **kwargs)  # call the function
        print("After calling " + func.__name__)
        return result
    return func_wrapper  # return reference to function object


# 1. manually decorating
def f1(a, b):
    return a+b


f1 = my_decorator(f1)  # manual decoration
print(f1(1, 2))

# 2. w/ @


@my_decorator
def f1(a, b):
    return a+b


print(f1(1, 2))  # no need of manul decoration
