
brian = {
    "name" : "Brian",
    "age" : 33,
    "country of birth" : "America",
    "favorite language" : "Python"
}


def userDict(dict):
    keys = dict.keys()
    values = dict.values()
    for i in range(0,len(keys)):
        print "My {} is {}".format(keys[i],values[i])


# CD solution:

def print_dictionary_values(dic):
    for some_key, some_value in dic.iteritems():
        print "My" + " " + some_key + " " + "is" + " " + str(some_value)
        
        # alternate method:
        # concatenating variables to strings commonly done with the .format() method (can be used on any string, or variable that
            # contains a string
        
        #print "My {} is {}".format(some_key, some_value)