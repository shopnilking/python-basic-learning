# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)


# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:

# for x in "banana":
#   print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:

# Exam the loop when x is "banana":

# fruits = ["apple", "banana", "cherry", "orange"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break


# fruits = ["apple", "mango", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         break
#     print(x)

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# for x in range(6):
#   print(x)
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6):

# Example
# Using the start parameter:

# for x in range(2, 6):
#   print(x)

# The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):


# for x in range(1,30,2):
#   print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# for x in range(6):
#   if x == 3:
#       break
#   print(x)
# else:
#   print("Finally finished!")


# Nested Loops
# A nested loop is a loop inside a loop.

# The "inner loop" will be executed one time for each iteration of the "outer loop":

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# The pass Statement
# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

# for x in [0, 1, 2]:
#     pass
