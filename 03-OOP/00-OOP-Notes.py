
### OBJECT ORIENTED PROGRAMMING ###

# 4 Pillars of OOP:
# 1. Abstraction: transitive attributes between objects of the same class
# 2. Encapsulation: compartmentalized attributes between objects of different classes
# 3. Inheritance: transitive attributes from parent to child classes
# 4. Polymorphism: child classes can have their own additional attributes and methods


# Class: A blueprint for the same type of objects. Instructions for how to build many objects that share characteristics.

# Object: A data type built according to specifications provided by the class definition. Also sometimes called an 'instance.' Programmers talk about 'instantiating' an object

# Two categories of class: Attributes and Methods
# 1. Attributes are variables inside a class / object. Values.
# 2. Methods are functions associated with a class / object. Logic.

# A unique class method called 'constructor' (in python, __init__) is run by a program to construct a new object. The constructor instantiates an object.

# Attributes and methods can be set as 'private' to individual objects
# Otherwise, they are 'public' and available to objects with the same class
# However, they are not available to their relational classes (see next)

# You can copy a class and create another class that is able to 'inherit' the original class attributes and methods. These are 'child' and 'parent' classes.
# - But these attributes and methods only apply to 'public' ones
# - But if you DID want to apply those attributes and methods, you could apply another attributes called 'protected' to apply them to children classes

# In short, OOP allows us to organize our code according to attributes & classes
# You can categorize your objects according to classes and their inherent attributes and methods

#EXAMPLE: WEBSITE USERS
# If creating an app with lots of instances of users, we need a system for creating a user based upon a set of instructions. What attributes and methods are common across all instances of users?


### Structure ###

# The keyword class creates a class named 'User'. It is the blueprint for creating objects (i.e. instances) of Users.
# Note one parameter defined: Object. When the parameter is an object, it means this class inherits from the 'object class'.

    class User(object):

# Next, some attributes and methods
# __init__ is the constructor
# __init__ is a magic method, automatically created and sometimes invoked whenever a new instance of a class is created
# New object creation includes passing parameters that initialize an object's attributes

        def __init__(self, name, email):
            
            # The following are instance variables (e.g. attributes)
            # The logic says: At user creation, set object attribute to argument entered
            self.name = name
            self.email = email
            self.logged = False

        # After user init with a name and email, we create a method
        # In any method, the first parameter will always be "self"
        # Self is implicit, since it's an object
        # In doing this, you can change the state of an object by making modifications to 'self'
        
        def login(self):
            self.logged = True
            print self.name + " is logged in."
            return self

        # Let's add a few more methods:

        def show(self):
        print "I am {}. My email is {}".format(self.name, self.email)
        return self
        
        def logout(self):
        self.logged = False
        print self.name + " is logged out."
        return self

# Now, let's create an instance of the class (object)
# Here we set a var, user12345, to class User, with two params (name and email)

user12345 = User("Brian Mendoza","bcmendoza@gmail.com")

# This then allows us to refer to user12345's attributes, which have already been set according to their class (User)

print user12345.name
print user12345.email

# How about for 'logged'? Depending on what method has been executed, printing 'logged' will return a boolean value.

print user12345.logged

# At this point, you have:

    # a class (User)
    # a magic __init__ method used only at object creation
    # three methods (login, show, logout)

# You set a user ID, user12345, to User, and passed arguments into its parameters:

    # self (passed implicitly by default)
    # 'name'
    # 'email'

# To use methods for that object, you simply call:

    # user12345.login()
    # user12345.show()
    # user12345.logout()

# But like in jQuery, you can also chain the methods:

    # user12345.login().show().logout()

# 'return self' at the end of each method returns the instance allowing you to chain another method after calling a method
# it is equivalent in jQuery to saying, 'return this'


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = True
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
    def logout(self):
        self.logged = False
        print self.name + " is not logged in"
        return self
    def show(self):
        print "My name is {}. You can email me at {}".format(self.name, self.email)
        return self