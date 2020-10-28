def knights(saying):
    def inner(quote):
        return "We are the knights who say: '% s'" % quote
    return inner(saying)


def knights2(saying):
    def inner2():
        # no argument, just use the outer parameter directly
        return "We are the knights who say: '% s'" % saying
    return inner2


a = knights('duck')
print(type(a))  # <class 'str'>
print(a)

a = knights2('duck')
print(type(a))  # <class 'function'>
# The inner2() function knows the value of saying that was passed in and remembers it.
print(a())  # "We are the knights who say: 'duck'"
