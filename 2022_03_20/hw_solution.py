# input 5
#     * * * * *
#    * * * * *
#   * * * * *
#  * * * * *
# * * * * *

# n = 5
# for x in range(n):
#     print(" "*(n-x-1), end="")
#     print("* "*n)

# input 5
# *****
# ****
# ***
# **
# *

# n = 5
# for x in range(n):
#     print("* "*(n-x))

# input 5
# *
# **
# ***
# ****
# *****

# n = 5
# for x in range(n):
#     print("* " * (x+1))


# input 5
#     *
#    **
#   ***
#  ****
# *****

# n = 5
# for x in range(n):
#     print(" "*(n-x-1), end="")
#     print("*"*(x+1))

# input 5
#     *
#    ***
#   *****
#  *******
# *********

# n=5
# for x in range(n):
#     print(" "*(n-x-1), end="")
#     print("*"*(x*2+1))


# input 5
# *********
#  *******
#   *****
#    ***
#     *

# n = 5
# for x in range(n):
#     print(" "*x, end="")
#     print("*"*(2*(n-x)-1))


# input 5
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
n = 5
for x in range(n):
    print(" "*(n-x-1), end="")
    print("*"*(x*2+1))
    
for x in range(n):
    if x==0:
        continue
    print(" "*x, end="")
    print("*"*(2*(n-x)-1))
