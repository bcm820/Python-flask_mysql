# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

def compareLists(list_one, list_two):

    if len(list_one) != len(list_two):
        print "Discrepancy: unequal list length."
        print "Result: The lists are not the same."
        return

    else:
        for i in range (0,len(list_one)):
            if list_one[i] == list_two[i]:
                pass
            else:
                print "Discrepancy:", list_one[i], "is not equal to", list_two[i]
                print "Result: The lists are not the same."
                return

    print "Result: The lists are the same."

compareLists([1,2,5,6,5,16],[1,2,5,6,5,8])