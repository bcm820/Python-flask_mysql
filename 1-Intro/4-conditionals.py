# conditionals work similar to JS

    if age >= 21:
        print 'Legal to drink'
    else:
        print 'Too young'

# but else-if statements = elif

    elif age > 40:
        print 'Too old to party'

# you can search a list to see if an item is inside

    groceryList = ["beef stock", "thyme", "pearl onions", "cremini mushrooms"]

    if "carrots" not in groceryList:        # not = !
        groceryList.append("carrots")       # in = used in for loops (e.g. for i in array)


# OPERATOR      DESCRIPTION

    # ==        Checks if equal
    # !=        Checks if not equal
    # <>        Checks if not equal (similar to !=)
    # >         Checks if greater than
    # <         Checks if lesser than
    # >=        Greater than or equal
    # <=        Less than or equal
    # and       Like && in JS
    # or        Like || in JS
    # not       Like ! in JS

# More: https://docs.python.org/2/library/stdtypes.html