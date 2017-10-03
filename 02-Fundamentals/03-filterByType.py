
# type = returns the type of an object
# isinstance = does the same, but also for subtypes?
# I'll learn more about this later

def filterByType(val):
    if type(val) == int:
        if val >= 100:
            print val, "- That's a big number!"
        else:
            print val, "- That's a small number!"
    if type(val) == str:
        if len(val) >= 50:
            print len(val), "chars: Long sentence."
        if len(val) < 50:
            print len(val), "chars: Short sentence."
    if type(val) == list:
        if len(val) >= 10:
            print len(val), "items: Big list!"
        if len(val) < 10:
            print len(val), "items: Short list."

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

filterByType(sI)
filterByType(mI)
filterByType(bI)
filterByType(eI)
filterByType(spI)
filterByType(sS)
filterByType(mS)
filterByType(bS)
filterByType(eS)
filterByType(aL)
filterByType(mL)
filterByType(lL)
filterByType(eL)
filterByType(spL)