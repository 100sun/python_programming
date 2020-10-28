# Python Programming

The material for this class is '[Introducing Python, 2nd Edition by Bill Lubanovic](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)'.

# Contents

### [1. A Taste of Py](#1-a-taste-of-py-1)

  + [Why Python](#why-python)
  + [Why not Python](#why-not-python)
  + [The Zen of Python, by Tim Peters](#the-zen-of-python-by-tim-peters)

### [2. Data](#2-data-1)

  + [Python Data Are Objects](#python-data-are-objects)
  + [What's in an python object?](#what's-in-an-python-object)
  + [Types](#types)
  + [Assignment](#assignment)
  + [Variables Are Names, Not Places](#variables-are-names-not-places)

### [3. Numbers](#3-numbers-1)

### [4. Choose with if](#4-choose-with-if-1)

### [5. Text Strings](#5-text-strings-1)

  + [formatting](#formatting)

### [6. Loop with while and for](#6-loop-with-while-and-for-1)

### [7. Tuples and Lists](#7-tuples-and-lists-1)

  + [Tuples](#tuples)
  + [Lists VS Dictionaries](#lists-vs-dictionaries)

### [8. Dictionaries and Sets](#8-dictionaries-and-sets-1)

  + [Sets](#sets)

### [9. Functions](#9-functions-1)

  + [Specify Default Parameter Values in None](#specify-default-parameter-values-in-none)
  + [Positional Arguments VS Keyword Arguments](#positional-arguments-vs-keyword-arguments)
  + [Docstrings](#docstrings)
  + [Inner Functions and Closures](#inner-functions-and-closures)
  + [Anonymous Functions: lambda](#anonymous-functions-lambda)
  + [Generators](#generators)
  + [Decorators](#decorators)
  + [Namespaces and Scope](#namespaces-and-scope)
  + [Uses of _ and __ in Names](#uses-of-_-and-__-in-names)
  + [Recursion](#recursion)
  + [Async Functions](#async-functions)
  + [Exceptions](#exceptions)

### [10. Oh Oh: Objects and Classes](#10-oh-oh-objects-and-classes-1)

  + [Object Oriented Paradigm](#object-oriented-paradigm)
  + [Class](#class)

<hr/>

# 1. A Taste of Py

``` py
# from library import function
import webbrowser
import json
from urllib.request import urlopen

site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
text = response.read().decode("utf-8")
data = json.loads(text)

# {'url': 'lolcats.com', 'timestamp': '20150613', 'archived_snapshots': {'closest': {'available': True, 'url': 'http://web.archive.org/web/20150610081618/http://www.lolcats.com/', 'timestamp': '20150610081618', 'status': '200'}}}

try:
    ## extract its value from a three-level Python dictionary.
    old_site = data["archived_snapshots"]["closest"]["url"]
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)
```

## Why Python

* simple and compact
* google-picked
* Data Science and Machine Learning

## Why not Python

* Static: C/C++, Java, Rust, Go
* Dynamic(script): Python PHP => low speed
* BUT std python interpreter in C is developing now

## The Zen of Python, by Tim Peters 

* Beautiful is better than ugly.
* Simple is better than complex. 
* Complex is better than complicated. 
* Readability counts. 

# 2. Data

* static lang: declare data type(o)
* **dynamic lang**: declare data type(x)

## Python Data Are Objects

* Python is rapping each data value(e.g. boolean / function..) as an object on the memory
* type ≒ class

``` py
type(7) # <class 'int'>
isinstance(7, type)
```

## What's in an python object?

* A *type* (ex. Integer)
* A unique *id* to distinguish it from other objects 
* A *value* consistent with its type (ex. 7)
* A *reference count* that tracks how often this object is used

``` 
a -> [int, a3494, 7, 1]
b -> [int, a3494, 7, 1]
```

## Types

* Py: Strong Type Lang => the *type* of an *object does not change*, even if its value is mutable
* mostly immutable values but mutable values: ***ByteArray, List, Set, Dictionary***
* bool / int / float / bytes(b'ab\ xff) / complex(5+9j) / str('alas', "alack", ''' a verse attack'''): all immutable values
* Integer List : ***mutable***. 

| Python Data Structures | mutable? | feature | comprehension |
| ---- | ----- | ---- | ---- |
| (tuple) | immutable | can be key of Dictionary | X |
| [⭐lists] | ***mutable*** | ordered | [~ for ~ in ~ if ~] |
| {set} | ***mutable*** | unordered, key(unique, immutable) | {~ for ~ in ~ if ~} |
| {⭐dict} | ***mutable*** | unordered, key(unique, immutable) : values(mutable) pairs | {~:~ for ~ in ~ if ~} |

## Assignment

* expression: A=B VS statement: A=B; 

## Variables Are Names, Not Places

* ∵ Python = Dynamic Lang & Interpreter Lang
* (re)assignment does not copy a value => **reference_count++**
* when reference_count == 0: **garbage collector**
    - can assign to **multiple** names

# 3. Numbers

``` py
# Booleans
int(True) # 1
bool(0.0) # False
# empty string, list, tuple, dictionary, set: False

# Integers
type(1_2_3) # <class 'int'>

# / floating-point (decimal) division 
5/1.1 # 4.545454
5/0.0 # python ZeroDivisionError / java infinity
# // integer (truncating) division
5//1.1 # 4.0
divmod(9,5) # (1,4)
# Python handles googoly(10^100) integers with no problem.

# Bases
bin() #0b
oct() #0o
hex() #0x

chr(65) ## = ord('A')
chr(97) ## = ord('a')
```

# 4. Choose with if

* block(x) indentation(o) ∵ Guido van Rossum loves to beautify 
* Continue Lines with \ (>80: recommended)
* if ~: elif ~: else: 
    - and, or, not, a < b < c
    - in (membership operator)

``` py
diff = tweet_limit - len(tweet_string)
if diff > = 0:
    print(" A fitting tweet")
```

``` py
# 'name := expression' (walrus operator)

if diff := tweet_limit - len( tweet_string) > = 0:
    print(" A fitting tweet")
```

# 5. Text Strings

* immutable string

* Create with 'a', "a", , """a""", '''(multi-line)''', str(a)
* str() -> (string formatting) => output
* \t, \n, \\, \', \", r'(raw-string)'
* replace('a', 'b', n_times): **didn't change the value** ∵ the interactive interpreter

* print(), the automatic echoing done by the interactive interpreter
* print(a, b): add a space VS a + b: no space
* +, *

* Get c with [ 0 || n || **-1** ]
* Get substr with [ start=0 : end=len() : step=1 ]

* split(default='\n', '\t', ' ') <-> ', '.join(str)
* strip(), lstrip(), rstrip() (==trim '\n', '\t', ' ')

* find(), rfind() : -1
* index(), rindex(): exception 
* count(), isalnum()

* CASE: capitalize(), upper(), lower(), swapcase()

* ALIGNMENT: center(30), ljust(30), rjust(30)

## formatting

``` py
# Old style: %
'% s' % 7.03

# New style: {} and format()
'The {:! ^ 10s} is at the {:! ^ 10s}'.format(thing, place) # 'The !! wraith!! is at the !! window!!'

# ⭐ Newest Style: f strings
thing = 'wereduck'
place = 'werepond'
f'The {thing} is in the {place}' 'The wereduck is in the werepond' # 'The wereduck is in the werepond'
f'The {thing: > 20} is in the {place:. ^ 20}' # 'The wereduck is in the ...... werepond......'
f'{thing = :>4.4}' # thing = 'were'
```

# 6. Loop with while and for

``` py
while/for ~:
    if: continue # VS c, java: continue in while loop and continue in for loop work different. ∵i++
    if: break    # else would be run if the while loop completed but the object was not found: 
else: # => break checker = break not called
```

``` py
for x in range(start, stop, step):
list(range(0, 11, 2)):
```

# 7. Tuples and Lists

In everyday programming, you’ll use **lists and dictionaries** more

### Tuples VS Lists

|lists|tuples|
|---|---|
|mutable|immutable => safe|
|多 functions| 少 space, speed⇑|
|comprehension 有|comprehension 無|

**Key** in the dict has to be **unique** -> almost string, and only **tuples** ∵ only immutable

## Tuples

### create

``` py
marx_tuple = 'a',
marx_tuple = 'a', 'b', 'c'
tuple(marx_list)
# tuple unpacking
a,b,c = marx_tuple
for first,second in tuple_list
# swap O without using temp
password, icecream = icecream, password
```

### add

* +: combine, *: duplicate, <>=: compare

``` py
t1 += t2
t1 # different from the above t1. It's new tuple. ∵immutable tuple
```

## Lists VS Dictionaries

| Lists | Dictionaries |
| ---- | ---- | 
| by offset| by **key** |
| **ordered**| unordered |

| action | Lists | Dictionaries |
| ---- | ---- | ---- | 
| create | [1, 'b', 3]<br/>list() | {'key'='value', }<br/>dict(key='value'), dict(two-level characters, strings, lists, tuples )|
| split | split(), list[::-2]  |  |
| add | **append**(str), **insert**(offset, str)<Br/>separator.join(friends) | dict[last_key]=last_val |
| combine | extend(b), += | a.update(b) | 
| combine(new) | a+b | {**a, **b} | 
| delete | **del** list[offset], **remove**('value'), **clear**(): delete all<br/>**pop**(0)=pop(-1)=tail, pop(0)=head| del<br/>clear()<br/>pop()| 
| sort | list.**sort**(reverse=true <Br/>new_list = list.**sorted**()| |
| get/find | **index**(value)<br/>value **in** list->True/False<br/>list.**count**(value), **len**(list) | dict[key]=value=**get**(key), **keys**(), **values**()<Br/>in<Br/>pairs=**items**(), pairs#=**len**(dict) |
| traverse | for in<Br/>zip() | for i in dict ≒ for i in dict.keys()<Br/>zip() |
| [copy](https://github.com/100sun/python_programming/blob/master/assignments/20181028%20%EB%B0%B1%EC%84%A0%ED%98%9C%20%EA%B3%BC%EC%A0%9C2.md#%EA%B0%80-%EC%84%A4%EB%AA%85) | b = a.copy() = list(a) = a[:]<br/>b = copy.**deepcopy**(a) | copy()<Br/>deepcopy() |
| compare | ==, !=, <> | ==, !=, **no ><** ∵ unordered |
| comprehension | [~ for ~ in ~ if ~] | { ~:~ for ~ in ~ if ~} |

### Lists

``` py
# zip(): iterate multiple sequences with zip()
for list1, list2, list3 in zip(list1, list2, list3):
list(zip(tuple1, tuple2))

# comprehension=
c_list = [number for number in range( 1, 6) if number % 2 = = 1]

# to modify the mutable list
list1[-1] = list1[-1].[::-1]
cap_list1 = '! '.join(i.capitalize() for i in list1)
```

### Dictionaries

``` py
dict(zip(tuple1, tuple2))
#comprehension
{letter: word.count(letter) for letter in set(word) if letter in vowels}

a = {1: 1, 2: 2, 3: 3}
b = {3: 3, 1: 1, 2: 2}
a == b # True

a = {1: [1, 2], 2: [1], 3:[ 1]}
b = {1: [1, 1], 2: [1], 3:[ 1]}
a == b # False
```

# 8. Dictionaries and Sets

## Sets

### create

* set(), {} (but empty {} == dict)
* len(), add(), remove(), in, for in
* Create an Immutable Set with frozenset()

### operator

* &, intersection(): A∩B
* |, union(): AUB
* -, difference(): A-B
* ^, symmetric_difference() : AUB-A∩B
* <=, issubset() / >=, issuperset() / > / <

### Comprehensions

``` py
# { ~ for ~ in ~ if ~}
a_set = {number for number in range(1, 6) if number % 3 = = 1}
```

# 9. Functions

## Specify Default Parameter Values in None

* None is a special Python value that holds a place when there is nothing to say.

``` py
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
def sol2(arg, result = None):
    if result is None:
        result = []
    result.append(arg)
    print(result)
```

## Positional Arguments VS Keyword Arguments

* Argument order: Required *positional* arguments < Optional positional arguments (*args) < Optional keyword arguments (** kwargs)

### Explode/Gather Positional Arguments with *

* def f1(n1, n2): positional argument
* def f1(*args): gather all those positional arguments into **a single args tuple**
    - => if parameter was a tuple -> args becomes one of of *two-level tuple*

``` py
print_args(*args) # the tuple of gathered arguments made in the func 
print_args(args) # the declared parameter value itself
```

### Explode/Gather Keyword Arguments with **

* def f1(n1=1, n2=2): keyword argument
* def f1(**kwargs): gather all those keyword arguments into the **a single kwargs dictionary**

### Define Keyword-Only Arguments with *

``` py
def print_data(data, *, start=0, end=100):
    print(data)
# they must be provided as name = value, not positionally as value.
print_data(data) #okay
print_data(data, start=4) #okay
print_data(data, 4) #notOkay
```

## Docstrings

``` py
def ~():
    'echo ~~' # declare function's docstring

help(echo) # print docstring
print(echo.__doc__) # print raw docstring
```

## Inner Functions and Closures

* inner: acts as a closure
* inner(): directly use the outer parameter
* inner() knows the value of saying that was passed in and remembers it.

``` py
def knights2(saying):
    def inner2(): # no argument, just use the outer parameter directly
        return "We are the knights who say: '% s'" % saying
    return inner2

a = knights2('duck')
print(type(a))  # <class 'function'>
print(a())  # The inner2() function knows the value of saying that was passed in and remembers it.
```

## Anonymous Functions: lambda

``` py
edit_story( stairs, lambda word: word.capitalize() + '!')
```

## Generators

||Function|Generator|
|--|--|--|
|returning|return value|yield iterator|

``` py
# comprehensions
genobj = (pair for pair in zip([' a', 'b'], [' 1', '2'])) 
print(list(genobj()) # generator object
# can be run only once
```

## Decorators

* a function that takes one function as input and returns another function.
* decorator returns a modified function or class.
* The modified functions or classes usually contain calls to the original function.
* @: just above the def runs first

``` py
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
print(f1(1, 2))  # no need of manual decoration
```

## Namespaces and Scope

``` py
locals() # returns a dictionary of the contents of the local namespace. 
globals() # a dictionary of the contents of the global namespace. (⊃ functions, the first class citizen)

global n # access global var
n = '2' # and change it
```

## Uses of _ and __ in Names

* the name of a function f: f.__name__
* its docstring: f.__doc__:

## Recursion

* when function calls itself => RecursionError: maximum recursion depth exceeded
* useful when list of lists of lists

``` py
def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            #1. py3.3~
                yield from flatten(item)
            #2. ~py3.3
            for subitem in flatten(item):
                yield subitem
        else:
            yield item
```

## Async Functions

* sync: default
* async: by *async* and *await*

## Exceptions

``` py
class myException(Exception): # make my own exception
    pass

try:
    raise myException # occur exception
except myException as myExpObj:  # make an exception obj
    print("error")

```

# 10. Oh Oh: Objects and Classes

## Object Oriented Paradigm

PIE

1. Encapsulation
2. Inheritance
3. Polymorphism

||C|Java|Python|
|--|--|--|--|
|object|by pointer/reference|by reference|by reference|
|multiple inheritance| O | X -> interface | O -> mro|

## Class

``` py 
class Cat:
pass

a_cat = Cat() # class obj
a_cat.age = 3 # access the attribute

class parent():

    def __init__(self, name): # initialization: the first one has to be self
        self.name=name # empty class

class child(parent): # issubclass(child, parent)

    def __init__(self, name, email):
        super().__init__(name) # inheritance
        self.email=email

cat.mro() # Method Resolution Order

# [<class '__main__.child'>, <class '__main__.parent'>, <class 'object'>]

# ifself -> parents -> grandparent -> ... -> type 
```
