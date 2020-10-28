print("*", end='')
print(f"your class is...{s_id%100%n+1}")
# dict
sentence = input("Type any sentence: ")
sentence = sentence.lower()
word_dict = {}
letter_dict = {}
for word in sentence.split():
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
print(f'Occurrence of each word: {word_dict}')
print(f'Occurrence of each letter: {letter_dict}')

#string
print("%sy Mc%sface" % (name.capitalize(), name.capitalize()))
print("{}y Mc{}face".format(name.capitalize(), name.capitalize()))
print(f"{name.capitalize()}y Mc{name.capitalize()}face")

surprise[-1] = surprise[-1][::-1]
cap_start1 = '! '.join(word.capitalize() for word in start1)
f2e = {e: f for f, e in e2f.items()}

for x in (f'Got {i}' for i in range(10)):
    print(x)

# none
def sol2(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

# inner
def knights2(saying):
    def inner2():
        # no argument, just use the outer parameter directly
        return "We are the knights who say: '% s'" % saying
    return inner2
a = knights2('duck')
print(a())  # <class 'function'>

# decorator
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

# exception
class myException(Exception):
    pass
try:
    raise myException
except myException as myExpObj:  # make exception obj
    print("error")

# generator
def gen_get_odds():
    for num in range(1, 10, 2):
        yield num
n = gen_get_odds()
print(list(n))

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))
print(list(genobj))
