# Odd/Even

def odd_even():
    for i in range(1, 201):
        if i % 2 == 1:
            print "Number is {}. This is an odd number.".format(i)
        if i % 2 == 0:
            print "Number is {}. This is an even number.".format(i)


# Multiply

def listMult(list, mult):
    list_mult = []
    for value in list:
        list_mult.append(value * mult)
    return list_mult


# Hacker Challenge
# Write a function that takes the multiply function call as an argument. Your new function should return the multiplied list as a two-dimensional list. Each internal list should contain the 1's times the number in the original list. Here's an example:

def layered_multiples(list_mult):
    list_1s = []                            # create empty list output of 1s
    for idx in range(0,len(list_mult)):     # FOR to iterate thru idxs of list_mult
        list_1s.append([])                  # Append empty sub-list into list_1s
        while list_mult[idx] > 0:           # FOR to divide up nums in each idx of list_mult
            list_1s[idx].append(1)          # Append 1 into sub-list until num < 1
            list_mult[idx] -= 1
    return list_1s


# CD Example Solution:

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array


# Will's 'hacky' solution: Turn 1s into strings and multiply them!

def layered_multiples(list_mult):
    list_1s = []
    for num in list_mult:
        list_1s.append(['1' * num])
    print list_1s