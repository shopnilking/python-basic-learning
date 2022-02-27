# input 5 ,6, add/sub/mul/div
# if add output is:11
# if sub output is:-1
# if mul output is: 30
# if div output is: 0


# input 5
# *
# **
# ***
# ****
# *****


# input 5
#     *
#    **
#   ***
#  ****
# *****

x = int(input("input number:"))
for i in range(x):
    print(" "*(x-i-1), end="")
    print("*"*(i+1))
