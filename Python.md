# To go further
- Learn about software development, architecture, principles and good practices
- Read documentation, and code of pairs (github, kaggle)
- Train on code gaming platforms (codingame)
# What you should know
- Complete roadmap : https://coggle.it/diagram/XgtVOa6K4obH730X/t/%F0%9F%90%8D%F0%9F%92%BB-python-developer-roadmap-%F0%9F%92%BB%F0%9F%90%8D/0b172b9775a0f8f50c3cda856b4e3bd59c3f7c53f53f63282d116d69447072fe

- Tools you'll spend hours with: https://missing.csail.mit.edu/

# Good practices
For anything, your code will be enhanced if you search for "good practices"

## Python
Python good practices
- PEP 8 (Python Enhancement Proposals)
- General: https://gist.github.com/sloria/7001839
- Guidelines: https://www.python.org/dev/peps/pep-0020/

# General Coding Practices
General guidelines for many languages:
- Code should be ordered in scripts (declare then use)
- Use multiple files: main, function, settings
- DRY: don't repeat yourself
- Use abstraction
- Respect naming conventions
- To go further, see Clean Code (Uncle Bob : https://www.youtube.com/watch?v=7EmboKQH8lM)

# Python concepts

# What you should know
- Complete roadmap : https://coggle.it/diagram/XgtVOa6K4obH730X/t/%F0%9F%90%8D%F0%9F%92%BB-python-developer-roadmap-%F0%9F%92%BB%F0%9F%90%8D/0b172b9775a0f8f50c3cda856b4e3bd59c3f7c53f53f63282d116d69447072fe
- Introduction to core tools: https://missing.csail.mit.edu/

# Official References
- Python Documentation: https://docs.python.org/3/
- Tutorial glossary: https://docs.python.org/3/glossary.html#glossary
- Tutorial: https://docs.python.org/3/tutorial/
- Reference: https://docs.python.org/3/reference/index.html#reference-index
- Built-in libraries glossary: https://docs.python.org/3/library/index.html#library-index
- Portal: https://docs.python.org/3/tutorial/whatnow.html

# Good practices and idioms
For anything, your code will be enhanced if you search for "good practices",
and will be closer to the generally accepted way of writing if you search for
"idiomatic python".
- PEP 8 (Python Enhancement Proposals)
- General: https://gist.github.com/sloria/7001839

## Concepts from New versions
- https://python.plainenglish.io/killer-features-by-python-version-c84ca12dba8


## References
- https://docs.python.org/fr/3/library/stdtypes.html#string-methods

# Commands

## Files (I/O)
```Python
with open('foo.txt') as f:
    print(next(f))
```


## Iterators and Generators

### Iterators
```Python
class Count:
    """Infinite count from zero"""

    def __init__(self):
        self.num = 0

    def __iter__(self):
        # Enables for loop calls
        return self

    def __next__(self):
        # Here is the trick of generators
        self.num += 1
        return self.num
```

### Generators
Generators are neat implementations of iterators

#### Standard builder
```Python
def count():
    num=0
    while True:
        num+=1
        yield num
```
#### Quick builders
```Python
# Further use with next
gen_squares = (x**2 for x in num_list)

# Instant result
sum(x**2 for x in num_list)
```

#### References
- https://www.programiz.com/python-programming/iterator
- https://www.programiz.com/python-programming/generator


## Decorators
**The goal is to modify the behavior of the function**. For instance, it can add some condition that may call or block the initial function. It can also add other function calls before and after the initial function.

### Example

```Python
# Define
def func_origin(arg1):
    pass

func_origin = func_deco1(func_origin)

# Call
func_origin()
```

With *func_deco1* defined as follows:
```Python
def func_deco1(func):
    def decorate():
        print("do something before")
        func()
    return decorate
```


The following is used instead of the previous implementation in order to make it more obvious:
```Python
# Define
def func_deco1(func):
    def decorate():
        print("do something before")
        func()
    return decorate

@func_deco1
def func_origin(arg1):
    pass

# Call
func_origin()
```


### References
- https://realpython.com/primer-on-python-decorators
- https://www.python.org/dev/peps/pep-0318


# Main Libraries for Data Science

## Pandas
How to get a specific value in a DataFrame, and difference in the
calling / setting method because of the chain indexing which either returns
a view or a copy :
- https://stackoverflow.com/questions/25254016/pandas-get-first-row-value-of-a-given-column

Should one iterate over rows?
- https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas


# Advanced Python
Deep dive into each intermediate concept by looking at its specificities, core
parameters and good practices (python advanced dictionary / ...).

## Intermediate Concepts
- File wildcards
- Private variables
- single dispatch
- __slots__
- Qualified name
- MRO (method resolution order)
- Garbage collection
- Assert
- Typecasting
- Pointers
- Generators
- Decorators
- Closures
- Cache
- Special methods (= Magic methods)
- Map / Filter / Reduce
- Map / lambda
- User-defined (callable) types
- ABC
- Operator overloading
- Context managers
- Coroutines
- Concurrency
- Callback
- Multithread, multiprocessing
- Deadlocks, Livelocks
- With statement
- Metaprogramming
- Dynamic atttributes
- Hashability
- Lambda
- Nested List / Dict Comprehension
- *args, **kwargs
- @staticmethod, @classmethod
- Anonymous functions
- Packaging, unpacking
- Encodings, Unicode, bytes, binary bitwise operations
- GIL (Global Interpreter Lock)
- Shallow, deepcopy
- Mocking
- Iterators vs Iterables
- Recursive functions
- Memoisation (speed up recursive functions)
- Variable scope: global, local and nonlocal
- Zip
- Currying
- Cython extensions (https://realpython.com/cpython-source-code-guide/)
- Amdahl's Law
- Reduction operators
- Starvation
- Race conditions
- Method resolution order
- Super()
- Weak references
- Namespaces
- Sockets
- Serialization formats
- Bidirectional communication
- Exceptions (chaining)
- Dunders
- Cloning objects
- Namedtuples
- Records
- Multisets
- Sushi operator
- Iterator chains
- Sentinel value
- Sort using key
- __repr__
- Shifting operations

## Modules
- Collections
- Itertools
- Functools
- Numpy: fast array, numexpr
- Pandas: views, copies
- Asyncio
- Dis
- Futures
- PyQt5
- Decimal

## Ressources
- Python advanced practices: https://www.youtube.com/watch?v=OSGv2VnC0go
- Python advanced book: https://effectivepython.com/
