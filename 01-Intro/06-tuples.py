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

# More: https://docs.python.org/2/tutorial/datastructures.html


# Tuple as RETURN VALUES

# Functions can only return a single value, but by making that value a tuple, you can group many values and return them together
# This function reeturns both the circumstance and area of a circle of given radius r:

def get_circle_area(r):
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)


# WHY USE TUPLES:
# - Store grouped info in a way that other developers cannot modify sets of data that should be constant
# - When reading others' code, when you come across a tuple, it means it is a very important part of their program