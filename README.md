# Python Programming

The material for this class is '[Introducing Python, 2nd Edition by Bill Lubanovic](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/)'.

<hr/>

# Contents

#### Python Programming

#### 1. A Taste of Py

  + [library modules](#library-modules)
  + [Why Python](#why-python)
  + [Why not Python](#why-not-python)
  + [The Zen of Python, by Tim Peters](#the-zen-of-python-by-tim-peters)

#### 2. Data

  + [Python Data Are Objects](#python-data-are-objects)
  + [What's in an python object?](#what's-in-an-python-object)
  + [Types](#types)
  + [Assignment](#assignment)

#### 3. Numbers

#### 4. Choose with if

#### 5. Text Strings

  + [definition](#definition)
  + [function](#function)
  + [formatting](#formatting)

#### 6. Loop with while and for

#### 7. Tuples and Lists

  + [Tuples](#tuples)
    - [create](#create)
    - [add](#add)
  + [Tuples VS Lists](#tuples-vs-lists)
  + [Lists & Dictionaries](#lists--dictionaries)
  + [Lists VS Dictionaries](#lists-vs-dictionaries)

#### 8. Dictionaries and Sets

  + [Sets](#sets)
    - [create](#create)
    - [operator](#operator)
    - [Set Comprehensions](#set-comprehensions)

#### 9. Functions

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

#### 10. Oh Oh: Objects and Classes

  + [Object Oriented Paradigm](#object-oriented-paradigm)
  + [Class](#class)

<hr/>

# 1. A Taste of Py

### library modules

``` py

import webbrowser
import json

# from library import function

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

Python is rapping each data value(e.g. boolean / function..) as an object on the memory

## What's in an python object?

* A type (ex. Integer)
* A unique id to distinguish it from other objects 
* A value consistent with its type (ex. 7)
* A reference count that tracks how often this object is used

## Types

* Py: Strong Type Lang => the *type* of an *object does not change*, even if its value is mutable
* mostly immutable values but mutable values: ***ByteArray, List, Set, Dictionary***
* bool / int / float / bytes(b'ab\ xff) / complex(5+9j) / str('alas', "alack", ''' a verse attack'''): all immutable values
* Integer list : ***mutable***. 

| Python Data Structures | mutable? | for what | ex |
| ---- | ----- | ---- |
| [⭐lists](#Lists-&-Dictionaries)[] | ***mutable*** | **ordered** array + only string<br/>(array: unordered) | [' Winken' / 'Blinken' / 'Nod'] |
| [tuple](#Tuples)() | immutable | **immutable** list<br/>- Elements can't be added, removed or replaced after declaration. | (2 / 4 / 8) |
| [set](#Sets)([]) | ***mutable*** | **unique** list<br/> - Elements doesn't have order and duplicates. extremely fast. | set([ 3 / 5 / 7]) |
| [⭐dict](#Lists-&-Dictionaries){} | **mutable** | pair of **key and values** | {'game': 'bingo' / 'dog': 'dingo' / 'drummer': 'Ringo'} |
|[functions](#9-Functions)| immutable || def print():|

## Assignment

* expression VS statement
* Dynamic Lang: 
    - **Assignment** does not copy a value; it just **attaches a name** to the object that contains the data.
    - => type(), instance()
* Interpreter Lang:
    - reassigning => reference_count++; || reference_count == 0 (**garbage collector**)
    - can assign to **multiple** names

# 3. Numbers

* Booleans: int(True) -> 1 / bool(0.0) -> False
* Integers: 1_2_3 可 (in recent Java too)
    - /: floating-point (decimal) division 
        - ex. 5/0.0 -> python exception / java infinity
    - //: integer (truncating) division
    - divmod(9,5) -> (1,4)
    - Python handles googoly integers with no problem.
* Bases: 0b(inary), 0o(ctal), 0x(hex)
    - bin(), oct(), hdx()
    - chr(65) = ord('A'), chr(97) = ord('a')

# 4. Choose with if

* block(x) indentation(o) <- Guido van Rossum loves to beautify 
* Comment with #
* Continue Lines with \ (>80)
* if ~: elif ~: else: 
    - and, or, not, a < b < c
    - false (empty string, list, tuple, dictionary, set)
    - in (membership operator)
    - name := expression (walrus operator)

# 5. Text Strings

## definition

* immutable string
* base(empty string) is also string
* \t, \n, \\(\), r'(raw string)'
* ', ", (multi-line)''', """
* []: 0, 1, n, **-1**
* [ start : end : step ]: start ~ (end-1) offset skipping by step

## function

* print(a, b): add a space VS a + b: no space
* print() VS the automatic echoing done by the interactive interpreter
* str() -> (string formatting) => output
* len(str), split('\n', '\t', ' '), 'a'.join(str), 
* replace('a', 'b', n_times): didn't change the value <- the interactive interpreter
* strip(), lstrip(), rstrip() (==trim)
* find(), rfind() : -1 / index(), rindex(): exception / count(), isalnum()
* capitalize(), upper(), lower(), swapcase() / center(), ljust(), rjust()

## formatting

* Old style: %
* New style: {} and format() ex. {index}, {:!^10s}
* Newest Style: f' ~ {str.title()=} ~ '

# 6. Loop with while and for

* while: ~ else: ~ continue, break(cancel the closest loop)
* for ~ in ~: ~ else: ~ continue, break(cancel the closest loop)
    - for x in range(start, **stop**, step) / list(range(0, 11, 2))

# 7. Tuples and Lists

## Tuples

### create

* tuple unpacking
  + tupleA = 'a', 'b', 'c'
  + tupleA = ('a', 'b', 'c')
  + a, b, c = tupleA
  + to exchange values in one statement without using a temporary variable (o)
* tuple(): makes tuples from other things

### add

* +: combine, *: duplicate, <=>: compare, t1+=t2: **immutable** but can modify

## Tuples VS Lists

* lists: more functions
* tuples: less space, immutable so safe

## Lists & Dictionaries

| action | Lists | Dictionaries
| ---- | ---- | ---- | 
| create | [1, 'b', 3], list() | {'key'='value', }, dict(key='value'), dict(two-item lists, tuples, strings, characters)|
| delete | del: by Offset, remove(): by Value, clear(): delete all<br/>pop(): get + return tail, pop(0): return head, pop(-1): return tail | del, pop(), clear() | 
| assign | = | = |
| extend | append(): Add to the end, insert(): add by Offset <br/> +: combine, *: duplicate<Br/>Convert a List to a String with join()<Br/>: ', '. join(marxes) / separator.join(friends) | combine : {**a, **b}, update(b) | 
| split | split(), marxes[::-2]  |  |
| sort | sort(reverse=true): list itself, sorted(): copied list | |
| find |  index()<br/>in: True/False, count(), len() | [key], get(), keys(), values(), items() - pairs, len()<Br/>in |
| traverse | for and in<Br/> Iterate Multiple Sequences: zip() | for and in<Br/>- values(), items() |
| [copy](https://github.com/100sun/python_programming/blob/master/assignments/20181028%20%EB%B0%B1%EC%84%A0%ED%98%9C%20%EA%B3%BC%EC%A0%9C2.md#%EA%B0%80-%EC%84%A4%EB%AA%85) | shallow copy: b = a.copy() = list(a) = a[:]<br/>deep copy: b = copy.deepcopy(a) | copy(), deepcopy() |
| compare | ==, !=, <> | ==, !=, no >< ∵ unordered |
| comprehension | [number for number in range( 1, 6) if number % 2 = = 1] | {letter: word.count( letter) for letter in set( word) if letter in vowels} |

## Lists VS Dictionaries

* by offset vs by **key** 
* **ordered** vs unordered
* in **key**: has to be **unique** - almost string, and only **tuples** ∵ only immutable

In everyday programming, you’ll use **lists and dictionaries** more

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
