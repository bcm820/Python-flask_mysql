### RULES ###

# If using brackets, indentation rules don't apply



### Integer Methods ###

import random
random.random()     # returns a random float from 0 to 1
random.randint(a,b) # returns a random int between range a-b (incl.)

### Built-In ###

round(float)        # rounds float up or down
{:,}                # uses comma for thousands


### STRING METHODS ###
# Functions run on a string.

    # METHOD                    # OUTPUT
    last.upper()                # 'MENDOZA'
    last.count('doza')          # 1 (counts occurrences)
    last.endswith('doza')       # T/F (end with 'doza'?)
    last.find('doza')           # 3 (char index of first occurrence)
    last.replace('z','s',1)     # Replace 1st occurrence of 'z' with 's'
    last.isalnum()              # T/F (alphanumeric? letters and numbers only, no spaces or punc)
                                # also last.isalpha(), last.isdigit(), last.islower(), last.isupper()
    string.join(list)           # takes list and returns a concatenated string
    string.split()              # returns list of values where string is split (or splits at every place, turning each word into a list)


    chr(ord('a') + 1)           # increment letter (character order) -- also decrement


# More: https://docs.python.org/2.6/library/string.html



STRING INTERPOLATION - .format()


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




# OPERATOR      DESCRIPTION

    # ==        Checks if equal
    # !=        Checks if not equal
    # <>        Checks if not equal (similar to !=)
    # >         Checks if greater than
    # <         Checks if lesser than
    # >=        Greater than or equal
    # <=        Less than or equal
    # and       Like && in JS
    # or        Like || in JS
    # not       Like ! in JS

# More: https://docs.python.org/2/library/stdtypes.html




# Tuples are containers for a fixed sequence of data objects
# They are immutable

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

# It's optional to put tuples within parentheses

# To print all values inside a tuple, you can iterate using a for loop:
dog = ("Canis Familiaris", "dog", "carnivore", 12)
for data in dog:
    print data


### Built-in Tuple Functions ### Shares many of the same functions as for lists
max(sequence)           # returns the largest value in the sequence
sum(sequence)           # return the sum of all values in sequence
enumerate(sequence)     # used in a for loop context to return two-item-tuple for each item in the list indicating the index followed by the value at that index.
map(function, sequence) # applies the function to every item in the sequence you pass in. Returns a list of the results.
min(sequence)           # returns the lowest value in a sequence.
sorted(sequence)        # returns a sorted sequence




### DICTIONARY FUNCTIONS ###

    cmp (dict1, dict2)      # Compares two dictionaries: left, key names, and values; returns 0 if equal, or -1 if dict1 is larger, or 1 if dict2 is larger
    len()                   # total length of dictionary
    str()                   # produces string representation of dictionary


### DICTIONARY METHODS ###

    dict.clear()                        # Removes all dictionary elements
    dict.copy()                         # Returns a shallow copy dictionary
    dict.fromkeys(sequence, [value])    # create a new dictionary with keys from sequence and values set to [value]
    dict.get(key)                       # used to retrieve the value paired with the requested key
    dict.has_key(key)                   # used to inquire if a given key is available in a dictionary (otherwise returns false)
    dict.setdefault(key)                # similar to get(), but will set dict[key]=default if key is not already in dictionary
    dict.update(dict2)                  # adds dict2's key-value pairs to an existing dictionary


# Lists From Dictionaries
# Using items(), keys(), and values(), we can create lists from dictionaries

    dict.items()                        # returns a list of 2-tupls pairs (key and value)
    dict.keys()                         # return a list of dictionary keys
    dict.values                         # returns a list of dictionary values

# Example:

    data ={"house":"Haus","cat":"Katze","red":"rot"}
    print data.items()                  #[('house', 'Haus'), ('red', 'rot'), ('cat', 'Katze')]
    print data.keys()                   #['house', 'red', 'cat']
    print data.values()                 #['Haus', 'rot', 'Katze']


# Dictionaries From Lists
# We can also create dictionaries from lists

    dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    countries = ["Italy", "Germany", "Spain", "USA"]

    # Using zip(), we can combine two lists by indexes like a zipper

    country_specialities = zip(countries, dishes)