my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

# def dictToTuples(dict):
#     return dict.items()
# OR

def dictToTuples(dict):
    keys = dict.keys()
    values = dict.values()
    tuples_list = []
    for i in range(0,len(keys)):
        tuples = (keys[i], values[i])
        tuples_list.append(tuples)
    return tuples_list