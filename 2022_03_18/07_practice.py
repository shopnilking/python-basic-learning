# 1 2 3 4 5 6 7 8 9 10
# Print 1 to n
from turtle import end_fill, st


n = int(input('Enter a number:'))

# for x in range(1, n+1):
#     print(x, end=', ')

# Method 1
for x in range(1, n+1):
    if(x != n):
        print(x, end=', ')
    else:
        print(x)

# Method 2
# newList = []
# for x in range(1, n+1):
#     newList.append(str(x))

# print(', '.join(newList))
