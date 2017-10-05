def findCharacters (word_list, char):
    newlist = []
    for i in word_list:
        if i.find(char) > -1:
            newlist.append(i)
    print newlist

findCharacters(['hello','world','my','name','is','Anna'], 'o')