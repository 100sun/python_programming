# Python Programming

There are notes and codes I wrote in the class LC003800, python programming. The material for this class is '[Introducing Python](https://www.oreilly.com/library/view/introducing-python-2nd/9781492051374/), 2nd Edition by Bill Lubanovic'.
<hr/>
<details>
  <summary>1. Python Basic</summary>

# 1. Python Basic

## 1-2 small programs

### for

``` py

## ex 1-1

for loop in 1, "str" :
    print(loop)
```

### list

* list : order (o) array(o) : only string 
* set : order (x) array(o)

``` py

## ex 1-2

list = ["~", "~"]
```

### dictionary 

like hashmap, hashtable

``` py

## ex 1-3

dict = {
    "a" : "~" ,
    "b" : "~" 
    }
str = "a"
print(dict[str])
```

## 1-3 bigger programs

### library modules

``` py

## ex 1-4

import webbrowser
import json

## from library import function

from urllib.request import urlopen

site = input("Type a website URL: ")
era = input("Type a year, month, and day, like 20150613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (site, era)
response = urlopen(url)
text = response.read().decode("utf-8")
data = json.loads(text)

## {'url': 'lolcats.com', 'timestamp': '20150613', 'archived_snapshots': {'closest': {'available': True, 'url': 'http://web.archive.org/web/20150610081618/http://www.lolcats.com/', 'timestamp': '20150610081618', 'status': '200'}}}

try:
    ## extract its value from a three-level Python dictionary.
    old_site = data["archived_snapshots"]["closest"]["url"]
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", site)
```

## 1-5 Why Python

* simple and compact
* google-selected
* Data Science and Machine Learning

## 1-6 Disadvs

* Static: C/C++, Java, Rust, Go
* Dynamic(script): Python PHP

=> low speed</br>
but its std interpreter is by C -> developing now

### Popularity

## 1-11 The Zen of Python

by Tim Peters 

* Beautiful is better than ugly.
* Simple is better than complex. 
* Complex is better than complicated. 
* Readability counts. 

</details>
<details>
  <summary>2. Data</summary>

# 2. Data

static lang: declare data type(o)
**dynamic lang**: declare data type(x)

## Python Data Are Objects

Python is rapping each data value(boolean / function..) as an object on the memory

### In an object

* A type (ex. Integer)
* A unique id to distinguish it from other objects 
* A value consistent with its type (ex. 7)
* A reference count that tracks how often this object is used

## Types

Py: Strong Type Lang => Data value can be ***mutable***, not the data type

* bool / int / float / bytes(b'ab\ xff) / complex(5+9j) / str('alas', "alack", ''' a verse attack''')

<hr/>

| Python Data Structures | for what | ex |
| ---- | ----- | ---- |
| [lists](##Lists) | for **ordered** sequence of objects | [' Winken' / 'Blinken' / 'Nod'] |
| [tuple](##Tuples) | ***immutable*** list | (2 / 4 / 8) |
| set | **unique** list - Elements doesn't have order and duplicates. | set([ 3 / 5 / 7]) |
| dict | pair of **key and values** | {'game': 'bingo' / 'dog': 'dingo' / 'drummer': 'Ringo'} |

So just like reassigning an **integer**, it is pointing a new memory. But if you make an integer **list**, it is ***mutable***. 

## Assignment

* expression VS statement
* Dynamic Lang: 
    - **Assignment** does not copy a value; it just **attaches a name** to the object that contains the data.
    - => type(), instance()
* Interpreter Lang:
    - reassigning => reference_count++; || reference_count == 0 (**garbage collector**)
    - can assign to **multiple** names

</details>

<details>
  <summary>3. Numbers</summary>

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

</details>
<details>
  <summary>4. Choose with if</summary>

# 4. Choose with if

* block(x) indentation(o) <- Guido van Rossum loves to beautify 
* Comment with #
* Continue Lines with \ (>80)
* if ~: elif ~: else: 
    - and, or, not, a < b < c
    - false (empty string, list, tuple, dictionary, set)
    - in (membership operator)
    - name := expression (walrus operator)

</details>
<details>
  <summary>5. Text Strings</summary>

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

</details>
<details>
  <summary>6. Loop with while and for</summary>

# 6. Loop with while and for

* while: ~ else: ~ continue, break(cancel the closest loop)
* for ~ in ~: ~ else: ~ continue, break(cancel the closest loop)
    - for x in range(start, **stop**, step) / list(range(0, 11, 2))

</details>
<details>
  <summary>7. Tuples and Lists</summary>

# 7. Tuples and Lists

## Tuples

* tuple unpacking
  + a, b, c = tupleA
  + tupleA = 'a', 'b', 'c'
  + tupleA = ('a', 'b', 'c')
  + exchange (o)
* The tuple() conversion function makes tuples from other things
* +(combine), *(duplicate), <=>(compare)
* modify: **immutable** but can *t1+=t2*
  + id() when a variable name is pointing to a new value:

## Lists

list : order (o) array(o) : only string
set : order (x) array(o) 
Create with []
Create or Convert with list()
Create from a String with split()
Get an Item by [ offset ]
Get Items with a Slice
Add an Item to the End with append()
Add an Item by Offset with insert()
Duplicate All Items with *
Combine Lists by Using extend() or +
Change an Item by [ offset ]
Change Items with a Slice
Delete an Item by Offset with del
Delete an Item by Value with remove()
Get an Item by Offset and Delete It with pop()
Delete All Items with clear()
Find an Item’s Offset by Value with index()
Test for a Value with in
Count Occurrences of a Value with count()
Convert a List to a String with join()
Reorder Items with sort() or sorted()
Get Length with len()
Assign with =
Copy with copy(), list(), or a Slice
Copy Everything with deepcopy()
Compare Lists
Iterate with for and in
Iterate Multiple Sequences with zip()
Create a List with a Comprehension
Lists of Lists
Tuples Versus Lists
There Are No Tuple Comprehensions
Coming Up
Things to Do
