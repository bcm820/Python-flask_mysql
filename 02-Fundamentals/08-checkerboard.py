# Checkerboard
# Write a program that prints a 'checkerboard' pattern to the console.
# Your program should require no input and produce console output that looks like so:
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *
# * * * *
#  * * * *

def Checkerboard():
    stars = " * * * *"
    for i in range (0, 8):
        if stars.endswith(' '):
            stars = " * * * *"
        else:
            stars = "* * * * "
        print stars

# CD SOLUTION:

def checkerboard():
    for i in range(0, 8):
        if i%2 == 0:
            print "* " * 4
        else:
            print " *" * 4
