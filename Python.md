# Good practices
For anything, your code will be enhanced if you search for "good practices"

## Python
Python good practices
- General: https://gist.github.com/sloria/7001839

## Coding
General guidelines for many languages:
- Use multiple files: main, function, settings
- Use abstraction
- DRY: don't repeat yourself
- Respect naming conventions
- To go further, see Clean Code (Uncle Bob)



# Commands

## Files (I/O)
‘‘‘Python
with open('foo.txt') as f:
    print(next(f))
‘‘‘


## Iterators and Generators

### Iterators
‘‘‘Python
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
‘‘‘

### Generators

#### Standard builder
‘‘‘Python
def reverse(text):
    for elem in text[::-1]:
        yield elem
‘‘‘

#### Quick builders
‘‘‘Python
generate_squares = (x**2 for x in num_list)

sum(x**2 for x in num_list)
‘‘‘
