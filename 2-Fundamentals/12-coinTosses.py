def coinTosses():
    import random
    print "Starting the program..."
    heads = 0
    tails = 0
    for turn in range (1,5001):
        flip = round(random.random())
        if flip == 0:
            heads += 1
            print "Attempt #{}: Throwing a coin... It's a heads! ... Got {} heads so far and {} tails so far".format(turn, heads, tails)
        if flip == 1:
            tails += 1
            print "Attempt #{}: Throwing a coin... It's a tails! ... Got {} heads so far and {} tails so far".format(turn, heads, tails)
    print "Ending the program, thank you!"