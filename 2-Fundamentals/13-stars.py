
# Part I

def draw_stars(numlist):
    for nums in numlist:
        print "*" * nums


# Part II

def draw_stars(list):
    for item in list:
        if type(item) == int:
            print "*" * item
        else:
            print item[0].lower() * len(item)