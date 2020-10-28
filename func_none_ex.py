# it’s empty only in the first time it’s called. In the second time, result still has one item from the previous call:
def prob(arg, result=[]):
    result.append(arg)
    print(result)

# 1. no default parameter value, then declare it as an empty list later


def sol1(arg):
    result = []
    result.append(arg)
    print(result)

# 2. specify default parameter value as not empty, then declare it as an empty list


def sol2(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)


prob('a')
prob('b')
sol1('a')
sol1('b')
sol2('a')
sol2('b')
