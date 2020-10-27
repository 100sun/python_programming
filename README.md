# Python Programming

The material for this class is '[Introducing Python, 2nd Edition by Bill Lubanovic](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)'.

# Contents

### [1. A Taste of Py](#1-a-taste-of-py)

    - [library modules](#library-modules)
  + [Why Python](#why-python)
  + [Why not Python](#why-not-python)
  + [The Zen of Python, by Tim Peters](#the-zen-of-python-by-tim-peters)

### [2. Data](#2-data)

  + [Python Data Are Objects](#python-data-are-objects)
  + [What's in an python object?](#what's-in-an-python-object)
  + [Types](#types)
  + [Assignment](#assignment)
  + [Variables Are Names, Not Places](#variables-are-names-not-places)

### [3. Numbers](#3-numbers)

### [4. Choose with if](#4-choose-with-if)

### [5. Text Strings](#5-text-strings)

  + [definition](#definition)
  + [function](#function)
  + [formatting](#formatting)

### [6. Loop with while and for](#6-loop-with-while-and-for)

### [7. Tuples and Lists](#7-tuples-and-lists)

  + [Tuples](#tuples)
    - [create](#create)
    - [add](#add)
  + [Tuples VS Lists](#tuples-vs-lists)
  + [Lists & Dictionaries](#lists--dictionaries)
  + [Lists VS Dictionaries](#lists-vs-dictionaries)

### [8. Dictionaries and Sets](#8-dictionaries-and-sets)

  + [Sets](#sets)
    - [create](#create)
    - [operator](#operator)
    - [Set Comprehensions](#set-comprehensions)

### [9. Functions](#9-functions)

  + [None Is Useful](#none-is-useful)
  + [Specify Default Parameter Values](#specify-default-parameter-values)
  + [Positional Arguments VS Keyword Arguments](#positional-arguments-vs-keyword-arguments)
    - [Explode/Gather Positional Arguments with *](#explodegather-positional-arguments-with-)
    - [Explode/Gather Keyword Arguments with **](#explodegather-keyword-arguments-with-)
    - [Keyword-Only Arguments](#keyword-only-arguments)
  + [Mutable and Immutable Arguments](#mutable-and-immutable-arguments)
  + [Docstrings](#docstrings)
  + [Functions Are First-Class Object](#functions-are-first-class-object)
  + [Inner Functions and Closures](#inner-functions-and-closures)
  + [Anonymous Functions: lambda](#anonymous-functions-lambda)
  + [Generators](#generators)
  + [Decorators](#decorators)
  + [Namespaces and Scope](#namespaces-and-scope)
  + [Uses of _ and __ in Names](#uses-of-_-and-__-in-names)
  + [Recursion](#recursion)
  + [Async Functions](#async-functions)
  + [Exceptions](#exceptions)

### [10. Oh Oh: Objects and Classes](#10-oh-oh-objects-and-classes)

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
* Integer list : ***mutable***. 

| Python Data Structures | mutable? | for what | ex |
| ---- | ----- | ---- | ---- |
| [⭐lists](#Lists-&-Dictionaries)[] | ***mutable*** | **ordered** array + only string<br/>(array: unordered) | [' Winken' / 'Blinken' / 'Nod'] |
| [tuple](#Tuples)() | immutable | **immutable** list<br/>- Elements can't be added, removed or replaced after declaration. | (2 / 4 / 8) |
| [set](#Sets)([]) | ***mutable*** | **unique** list<br/> - Elements doesn't have order and duplicates. extremely fast. | set([ 3 / 5 / 7]) |
| [⭐dict](#Lists-&-Dictionaries){} | ***mutable*** | pair of **key and values** | {'game': 'bingo' / 'dog': 'dingo' / 'drummer': 'Ringo'} |
|[functions](#9-Functions)| immutable || def print():|

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
|多 functions| 少 space|
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

### Lists VS Dictionaries

| Lists | Dictionaries |
| ---- | ---- | 
| by offset| by **key** |
| **ordered**| unordered |

| action | Lists | Dictionaries |
| ---- | ---- | ---- | 
| create | [1, 'b', 3]<br/>list() | {'key'='value', }<br/>dict(key='value'), dict(two-level characters, strings, lists, tuples )|
| split | split(), list[::-2]  |  |
| add | **append**(str), **insert**(offset, str), **extend**(merge)<br/> +: combine, *: duplicate, +=: merge<Br/>separator.join(friends) | combine : {**a, **b}, update(b) | 
| delete | **del** list[offset], **remove**('value'), **clear**(): delete all<br/>**pop**(0)=pop(-1)=tail, pop(0)=head| del, clear()<br/>pop()| 
| assign | = | = |
| sort | list.sort(reverse=true <Br/>new_list = list.sorted()| |
| find |  index()<br/>in: True/False, count(), len() | [key], get(), keys(), values(), items() - pairs, len()<Br/>in |
| traverse | for and in<Br/> Iterate Multiple Sequences: zip() | for and in<Br/>- values(), items() |
| [copy](https://github.com/100sun/python_programming/blob/master/assignments/20181028%20%EB%B0%B1%EC%84%A0%ED%98%9C%20%EA%B3%BC%EC%A0%9C2.md#%EA%B0%80-%EC%84%A4%EB%AA%85) | shallow copy: b = a.copy() = list(a) = a[:]<br/>deep copy: b = copy.deepcopy(a) | copy(), deepcopy() |
| compare | ==, !=, <> | ==, !=, no >< ∵ unordered |
| comprehension | [number for number in range( 1, 6) if number % 2 = = 1] | {letter: word.count( letter) for letter in set( word) if letter in vowels} |

``` py
# zip(): iterate multiple sequeces with zip()
for list1, list2, list3 in zip(list1, list2, list3):
list(zip(tuple1, tuple2))
# comprehension: [- for - in - if -]
c_list = [number for number in range( 1, 6) if number % 2 = = 1]
{letter: word.count( letter) for letter in set( word) if letter in vowels}
```

# 8. Dictionaries and Sets

## Sets

* A list by using square brackets ([]) 
* A tuple by using commas and optional parentheses 
* A dictionary or set by using curly brackets ({}) 
  + For the set, it’s either there or it’s not; there’s no index or key:

### create

* set(), {} (but empty {} == dict)
* len(), add(), remove(), in, for in
* Create an Immutable Set with frozenset()

### operator

* &, intersection()
* |, union()
* -, difference()
* ^, symmetric_difference()
* <=, issubset(), >=, issuperset(), >, <

### Set Comprehensions

* a_set = {number for number in range( 1, 6) if number % 3 = = 1}

# 9. Functions

## None Is Useful

* None is a special Python value that holds a place when there is nothing to say.

## Specify Default Parameter Values

``` py

# it’s empty only the first time it’s called. The second time, result still has one item from the previous call:

def buggy(arg, result=[])

# 1. no default parameter value, then declare it as an empty list later

def works(arg):
    result = []

# 2. specify default parameter value as not empty, then declare it as an empty list

def nonbuggy(arg, result = None):
    if result is None:
        result = []
```

## Positional Arguments VS Keyword Arguments

Argument order

1. Required *positional* arguments
2. Optional positional arguments *(*args)*
3. Optional keyword arguments *(** kwargs)*

### Explode/Gather Positional Arguments with *

*args

* when calling: explode that tuple to the positional arguments
    - if it was a tuple -> also single tuple
* when defining: gather all those positional arguments into a single tuple of parameter values
    - if it was a tuple -> because one tuple of two-level tuple

### Explode/Gather Keyword Arguments with **

**kwargs

* when calling: explode a dictionary kwargs into name = value arguments
* when defining: gather name = value keyword arguments into the single dictionary parameter kwargs.

### Keyword-Only Arguments

``` py

# they must be provided as name = value, not positionally as value.

print_data(data) #okay
print_data(data, start=4) #okay
print_data(data, 4) #notOkay
```

## Mutable and Immutable Arguments

That was because the list was mutable and the integer and string were immutable.

``` py
arg[1] = "~" # changed the second object of a list
```

## Docstrings

``` py
def ~():
    'echo ~~' # declare function's docstring

help(echo) # print docstring
print(echo.__doc__) # print raw docstring
```

## Functions Are First-Class Object

``` py

# both objects(variable and function) point to same address.

f1=func()

print(f1 is func) #True 
```

## Inner Functions and Closures

``` py
def knights(saying):
    def inner(quote):
        return "We are the knights who say: '% s'" % quote
    return inner(saying)

# closure

def knights2(saying):
    def inner2(): # inner2() uses the outer saying parameter directly instead of getting it as an argument.
        return "We are the knights who say: '% s'" % saying
    return inner2

# The inner2() function knows the value of saying that was passed in and remembers it. 

>>> a=knights2('duck')
>>> type(a)
<class 'function'> # <class 'str'>
>>> a()
"We are the knights who say: 'duck'" # so str obj is not callable => err
>>> a
<function knights2.<locals>.inner2 at 0x00000166DDC1AEE0> # "~~"
```

## Anonymous Functions: lambda

``` py
edit_story( stairs, lambda word: word.capitalize() + '!')
```

## Generators

: sequence creation object

* can be run only once

``` py
>>> def get_odds(): 
	for num in range(1,10,2):
		yield num ### instead of return

>>> get_odds # function
>>> get_odds() # generator object
>>> cnt = 1
>>> for num in get_odds():
	if cnt == 3:
		print(num)
		break
	cnt += 1

5
>>> genobj = (pair for pair in zip([' a', 'b'], [' 1', '2'])) 
>>> for num in genobj: # generator object
```

## Decorators

: a function that takes one function as input and returns another function.

* just above the def(@~) runs first

``` py
>>> def test(func):
	def new_func(*args, **kwargs): # Inner functions w/ *args and ** kwargs
		print('start')
		result = func(*args, **kwargs) # Functions as agruments
		print('end')
		return result
	return new_func

>>> 

# manual_dec_func() = test(dec_func) # manual decorator assignment

>>> @test
def dec_func():
	print("This was decorated to the decorator @test")

# manual_dec_func(put arg)

>>> dec_func()
start
This was decorated to the decorator @test
end
>>> 
```

## Namespaces and Scope

* namespace in main: global scope
    - globals() returns a dictionary of the contents of the global namespace.(⊃ functions, the first class citizen)
* namespace in func: local scope
    - locals() returns a dictionary of the contents of the local namespace. 
* how to change: **global** ~ \n ~ = ''

## Uses of _ and __ in Names

* the name of a function: function.__name__
* its docstring: function.__doc__:

## Recursion

* Python saves the universe again by raising an exception if you get too deep
    - RecursionError: maximum recursion depth exceeded

``` py
def flatten(lol):
    for item in lol:
        if isinstance(item, list):
            # yield from flatten(item)
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
try:
    ~~
except IOException as error_name:
    ~~
```

# 10. Oh Oh: Objects and Classes

## Object Oriented Paradigm

PIE

1. Encapsulation
2. Inheritance
3. Polymorphism

object = pointer/reference(c++) = reference(java) = reference(python)

## Class

* attributes: class **.** attribute
* multiple inheritance: c++(o) java(x->interface) python(o) by mro

``` py 
class cat():

    pass

cat.mro() # Method Resolution Order: itself -> first-second parent -> grandparent ...

class parent():

    def __init__(self, name): # initialization: the first one has to be **self**
        self.name=name # empty class

class child(parent): # issubclass(child, parent)

    def __init__(self, name, email):
        super().__init__(name)
        self.email=email

```
