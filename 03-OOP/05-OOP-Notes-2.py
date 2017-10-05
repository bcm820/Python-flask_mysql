
### MODULES ###

# Modules are Python files (.py) you import to initialize and use its functions
# They only need to be initialized once

    import myfunctions  # assumes .py file extension

# Python comes with many built-in modules:
# https://docs.python.org/2/library/index.html

# You can read documentation on built-in modules via:

    dir(module)     # prints a list of functions
    help(module)    # prints detailed info on the module

# A PACKAGE is a collection of modules in directories with a package hierarchy

    # Project
    #     |_____ CURRENT_FILE.py
    #     |_____ my_modules
    #             |_____ __init__.py
    #             |_____ test_module.py
    #             |_____ another_module.py

# Each package MUST contain a special file called:

    # __init__.py

    # This file can be empty, but indicates a package that can be imported
    # In the above example, the package, "my_modules" has the __init__.py

# To import the modules inside of a package, we call them in two ways:

    import my_modules.test_module

    # OR

    from my_modules import another_module.py

    # The modules have been imported into CURRENT_FILE.py

# Using methods from imported modules in packages

    from datetime import datetime   # from datetime package, import datetime module
    print datetime.now()    # Uses .now() method to print current time of datetime object
    print datetime.now().strftime("%m/%d/%Y") # Formatted for usability

    from random import random, randrange # from random package, import randrange module
    print random()          # Calls random() method
    print randrange(1,11)   # Calls randrange() method



### MULTIPLE ARGUMENTS ###

# To pass multiple arguments into a single parameter, you can:

    def function(*args):
        # Insert code

    function("one", 2, [3])

    # When a param is prefixed with an asterisk (the "splat" operator), all the arguments passed in are bundled into a new tuple, which is then assigned to that parameter



### INHERITANCE ###

class Person(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def say(self, thing):
        print self.name, "says", thing

    # To create a child class (subclass), you pass the Parent class in as an arg
    class Student(Person):

        def __init__(self, name, email):
            # 'super' runs methods in the parent class
            # This will be discussed later
            super(Student, self).__init__(name, email)
            self.numberOfBelts = 0

        def addBelt(self):
            self.numberOfBelts += 1
            return self

        def say(self):
            # call the say method from the parent class
            super(Student, self).say("thing")
            # add to the previous method (but only for itself)
            print self.name, "says something else"

# To create updated versions of methods defined in a parent class for a child class, you should reference that parent object with the keyword 'super':

    super(ChildClassName, self).parent_method()

# One thing we may want to do is call the Parent's __init__ method, but also have our Child class chang eattributes defined by its parent class. Example:

    class Wizard(Human):                    # Parent class = human
        def __init__(self):
            super(Wizard, self).__init__()   # use super to call the Human __init__ method
            self.intelligence = 10           # every wizard starts off with 10 intelligence
        def heal(self):
            self.health += 10