def typeList(l):
    
    # Create unique lists based on type
    l_str = []
    l_int = []
    
    # Identify each item type and append to lists
    for i in l:
        if type(i) == str:
            l_str.append(i)
        if type(i) == int or type(i) == float:
            l_int.append(i)
    
    # Sum integers
    total = 0
    for i in l_int:
        total += i
    
    # Identify list type(s) and print output(s)
    if len(l_str) > 0:
        strings = " "
        if len(l_int) > 0:
            print "The list you entered is of mixed type"
            print "String:", strings.join(l_str)
            print "Sum:", total
        else:
            print "The list you entered is of string type"
            print "String:", strings.join(l_str)
    else:
        print "The list you entered is of integer/float type"
        print "Sum:", total

typeList(['magical unicorns',19,'hello',98.98,'world'])
typeList([2,3,1,7,4,12])
typeList(['magical','unicorns'])
