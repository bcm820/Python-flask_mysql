# define a function that says hello to name

    def say_hello(name):
        # indented lines are part of a function
        if name:
            print 'Hello, ' + name
        else:
            print 'No name'

# call function like this:

    say_hello('Brian')

# concat using comma or +, like in JS

    first = Brian
    print "My name is", Brian   # includes space
    print "My name is" + Brian  # no space

# use curly brackets to inject variables
# i.e. string interpolation

    last = "Mendoza"
    print "My name is {} {}".format(first, last)

### Old Depcrecated Method ###

    hw = "hello %s" % 'world'
    print hw    # prints 'hello world'



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

# More: https://docs.python.org/2.6/library/string.html
