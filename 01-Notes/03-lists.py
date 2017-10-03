# Lists are similar to arrays in JS
# Lists can mix data types

    fruits = ['apple', 'banana']
    vegetables = ['lettuce', 'carrot']

# you can add and output will print list in order

    fruits_and_veggies = fruits + vegetables    # ['apple', 'banana', 'lettuce', 'carrot']

# you can even multiply

    salad = vegetables * 2      # ['lettuce', 'carrot', 'lettuce', 'carrot']


### LIST METHODS ###

    fruits.append('orange') # Adds 'orange' to fruits
    salad[1:3]              # List range 1-2 (not incl. last digit)
    len(salad)              # Amt of items in list
    salad.extend(fruits)    # Adds fruit list to salad
    salad.pop(1)            # Removes salad[1] (carrot); if blank, pops last item
    salad.index('carrot')   # 1; Gives position in list based on word parameter

# More: http://www.linuxtopia.org/online_books/programming_books/python_programming/python_ch14s07.html


# Sequences = lists over which we can iterate, including tuples and strings


### SEQUENCE METHODS ###

    enumerate(salad)            # ??? used in a FOR loop context to return two-item-tuple for each item in list indicating the index followed by the value at that index
    map(function, salad)        # applies function to every item in the sequence and returns a list of the results!
    min(salad)                  # returns the smallest value in a sequence; for strings, compares alphabetically
    max(salad)                  # returns the largest value in a sequence
    sorted(salad)            # returns a sorted sequence; for strings, sorts alphabetically

# More: https://docs.python.org/2/library/functions.html