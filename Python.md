# What you should know
- Complete roadmap : https://coggle.it/diagram/XgtVOa6K4obH730X/t/%F0%9F%90%8D%F0%9F%92%BB-python-developer-roadmap-%F0%9F%92%BB%F0%9F%90%8D/0b172b9775a0f8f50c3cda856b4e3bd59c3f7c53f53f63282d116d69447072fe

- Tools you'll spend hours with: https://missing.csail.mit.edu/

# Good practices
For anything, your code will be enhanced if you search for "good practices"

## Python
Python good practices
- PEP 8 (Python Enhancement Proposals)
- General: https://gist.github.com/sloria/7001839

## Coding
General guidelines for many languages:
- Code should be ordered in scripts (declare then use)
- Use multiple files: main, function, settings
- DRY: don't repeat yourself
- Use abstraction
- Respect naming conventions
- To go further, see Clean Code (Uncle Bob : https://www.youtube.com/watch?v=7EmboKQH8lM)



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
