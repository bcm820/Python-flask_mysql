
# A dictionary is a mutable set type that consists of pairs (items) of keys and corresponding values
# It is the same thing as an associative array or hash table in other languages
# In general, a hash table is the most generic term

# General characteristics:

    # - An unordered collection of objects
    # - Values accessed using a key
    # - Able to shrink or grow as needed
    # - Can be modified
    # - Can hold other dictionaries (nested)
    # - Can't use sequence operations (e.g. slicing)

# While lists are closed by brackets [],
# and tuples are closed by parentheses (),
# dictionaries are closed by braces {}
# and use keys to track position rather than an index.

# Dictionaries can be made using literal notation:

    weekend = {"Sun": "Sunday", "Sat": "Saturday"}

# But also, they can be made by adding values one by one:

    capitals = {} #create an empty dictionary then add values
    capitals["svk"] = "Bratislava"
    capitals["deu"] = "Berlin"
    capitals["dnk"] = "Copenhagen"

# EACH KEY IN A DICTIONARY MUST BE UNIQUE

# To access values of a dictionary, you can use square brackets along with the key:

    print weekend["Sun"]
    print capitals["svk"]

# You can use a FOR loop to access all keys and values:

    #to print all keys
    for data in capitals:
        print data

    #another way to print all keys
    for key in capitals.iterkeys():
        print key

    #to print the values
    for val in capitals.itervalues():
        print val
        
    #to print all keys and values
    for key,data in capitals.iteritems():
        print key, " = ", data

    

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
    dict.iteritems()                    # Returns an iterator over the dictionary's key-value pairs


# Nested Dictionaries are also allowed

    context = {
    'questions': [
    { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
    { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
    { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
    { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
    ]
    }

# To iterate the values of a nested dictionary, use a nested FOR loop:

    for key, data in context.items():
        for value in data:
            print "Question #", value["id"], ": ", value["content"]

    # OUTPUT:
    # Question # 1 :  Why is there a light in the fridge and not in the freezer?
    # Question # 2 :  Why don't sheep shrink when it rains?
    # Question # 3 :  Why are they called apartments when they are all stuck together?
    # Question # 4 :  Why do cars drive on the parkway and park on the driveway?


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
    print country_specialities
    # Result is...
    # [('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]
    # The variable country_specialities now contains the dictionary in the 2-tuple list form
    # This form can easily be transformed into a real dictionary with the function dict()

        country_specialities_dict = dict(country_specialities)
        print country_specialities_dict
        # RESULT: {'Germany': 'sauerkraut', 'Spain': 'paella', 'Italy': 'pizza', 'USA': 'hamburger'}

    # But what if one list is longer than another? Easy: The extra elements will not be used in the combined tuples
    countries = ["Italy", "Germany", "Spain", "USA", "Switzerland"]
    dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
    country_specialities = zip(countries,dishes)
    print country_specialities
    # RESULT: [('Italy', 'pizza'), ('Germany', 'sauerkraut'), ('Spain', 'paella'), ('USA', 'hamburger')]