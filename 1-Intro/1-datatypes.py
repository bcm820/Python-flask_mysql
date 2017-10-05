# Primitive data types:

    # booleans
    true
    false

    # numbers
    3           # integers (whole numbers)
    4.5         # floats (decimal numbers)

    # strings
    'string'

# Composite data types:

    # Tuples: immutable list, holds a group of values (can be mixed)
    # Lists: mutable list of data
    # Dictionaries: group of key-value pairs; elements are indexed by unique keys used to access values

# Numbers and strings

    # For numbers declared as strings (e.g. x = '1'), you can call them as integers via int()
    x = '1'
    int(x)  # output is: 1

    # You can also call integers as strings via str()
    y = 2
    str(y)

    # You cannot concatenate an integer with a string, however
    x + you     # will return an error; cannot concatenate 'str' and 'int' objects