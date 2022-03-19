# input 5
# *****
# *****
# *****
# *****
# *****

# input 5
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# n = int(input('Enter a number:'))

# Method 1
n = int(input('Enter a number:'))
for x in range(n):
    for y in range(n):
        if(y == n-1):
            print("*")
        else:
            print("*", end=" ")

# Method 2
# n = 5
# for x in range(n):
#     print("* "*n)