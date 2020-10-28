# 9.1
def good():
    return ['Harry', 'Ron', 'Hermione']


print(good())


# 9.2
def get_odds():
    for i in range(10):
        if i % 2 == 1:
            yield i


cnt = 0
for i in get_odds():
    cnt += 1
    if cnt == 3:
        print(i)

# 9.3


def test(func):
    def func_wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return func_wrapper


@test
def f1(a, b):
    return a+b


print(f1(1, 2))
# 9.4


class OopsException (Exception):
    pass


try:
    raise OopsException
except OopsException:
    print('Caught an oops')


class myException(Exception):
    pass


try:
    raise myException
except myException as myExpObj:  # make exception obj
    print("error")


class parent():

    def __init__(self, name):  # initialization: the first one has to be self
        self.name = name  # empty class


class child(parent):  # issubclass(child, parent)

    def __init__(self, name, email):
        super().__init__(name)  # inheritance
        self.email = email


print(child.mro())
print(parent.mro())
