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

*  ***list***: [' Winken' / 'Blinken' / 'Nod']
* ***dict***: {'game': 'bingo' / 'dog': 'dingo' / 'drummer': 'Ringo'} 
* tuple: (2 / 4 / 8)
* ***set***: set([ 3 / 5 / 7]) 
* frozenset([' Elsa' / 'Otto'])
* ***bytearray***(bytearray(...))

So just like reassigning an **integer**, it is pointing a new memory. But if you make an integer **list**, it is ***mutable***. 

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
