# Find and replace
# Print the position of the first instance of 'day'
# Create a copy where 'day' is replaced with 'month'

    words = "It's thanksgiving day. It's my birthday, too!"
    print words.find('day')
    words_copy = words.replace('day','month',1)
    print words_copy

# Min and Max
# Print the min and max values in a list

    x = [2,54,-2,7,12,98]
    print min(x)
    print max(x)

# First and Last
# Print the first and last values in a list
# Create a copy containing only the first and last values

    x = ["hello",2,54,-2,7,12,98,"world"]
    print x[0]
    print x[len(x)-1]
    x_copy = [x[0], x[len(x)-1]]

# New List
# Start with a list: x = [19,2,54,-2,7,12,98,32,10,-3,6]
# Sort it
# Split it in half
# Push the list created from the first half to position 0 of the list created from the second half
# Output should be: [[-3, -2, 2, 6, 7], 10, 12, 19, 32, 54, 98]

    x = [19,2,54,-2,7,12,98,32,10,-3,6]
    x = sorted(x)
    x1 = x[0:len(x)/2]
    x2 = x[len(x)/2:]
    x2 = [[x1] + x2]