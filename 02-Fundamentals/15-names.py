
# Part I
# Given the following list, create a program that outputs full names (e.g. "Michael Jordan")

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def printDictVals(list_of_dicts):
    for dict in list_of_dicts:
        values = dict.values()
        string = " ".join(values)
        print string


# Part II
# Given the folllowing dictionary, create a program that prints the following format:
# Students
# 1 - MICHAEL JORDAN - 13
# ...

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printDictLen(dict_of_dicts):
    for key, value in dict_of_dicts.iteritems():
        print key
        count = 0
        for dict in value:
            string = (" ".join(dict.values()))
            count += 1
            print count, "-", string.upper(), "-", len(string) - 1


# CD SOLUTION

def show_students(arr):
    for student in students:
        print student['first_name'], student['last_name']

def show_all(users):
    for role in users:
        counter = 0
        print role
        for person in users[role]:
            counter += 1
            first_name = person['first_name'].upper()
            last_name = person['last_name'].upper()
            length = len(first_name) + len(last_name)
            print "{} - {} {} - {}".format(counter, first_name, last_name, length)