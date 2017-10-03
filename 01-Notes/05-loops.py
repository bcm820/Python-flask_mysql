# Two ways to FOR loop (for when you know how long your loop should run)

    # the range method: most common
    for count in range (1,6):   # range creates an array
        print count             # prints integer on separate line, updates value of count

    # the not-range method: when looping through a list or sequence
    array = [1, 2, 3, 4, 5]
    for count in array:
        print count             # prints integer on separate line, updates value of i

# To WHILE loop (for when it is unclear when your loop might need to stop)

    # you can write the previous loops this way (takes longer in general)
    count = 1
    while count < 5:
        print count
        count += 1

# you can also loop strings!!!

    for val in "string":        # output will be:
        if val == "i":          # s
            break               # t
        print val               # r

    for val in "string":        # output will be:
        if val == "i":          # s
            continue            # t
        print val               # r
                                # n
                                # g

# you can use 'pass' statement as a null operation:

    for val in my_string:
        pass                    # nothing happens when executed
    
# you can also combine ELSE with loops!!!

    for val in range (1,6):
        print val
    else:                       # after loop ends, cmd after else: is executed
        print "6 at the end"

    # BTW, if you exit the loop via a break or return, the 'else' will not run