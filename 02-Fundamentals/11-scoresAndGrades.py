def genScoresGrades():
    import random
    print "Scores and Grades"
    for i in range(1,11):
        score = random.randint(60,100)        
        if score <= 69:
            print "Score: {}; Your grade is D".format(score)
        elif score <= 79:
            grade = chr(ord('D') - 1)
            print "Score: {}; Your grade is C".format(score)
        elif score <= 89:
            grade = chr(ord('D') - 2)
            print "Score: {}; Your grade is B".format(score)
        elif score <= 100:
            grade = chr(ord('D') - 3)
            print "Score: {}; Your grade is A".format(score)
    print "End of the program. Bye!"

genScoresGrades()
