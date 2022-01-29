# x = "awesome" #global variable

# def myfunc():
#     x = "good"  #local variable
#     y = "amar sonar bangla"
#     print("Python is " + x)
#     print(y)
    
# def myfunc2():  
#     print("Python is " + x)
#     # print(y) #this variable can not accessable from this function
    

# myfunc()

# myfunc2()



# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

# Example
# If you use the global keyword, the variable belongs to the global scope:


# def myfunc():
#   global x
#   x = "fantastic"
#   print("Python is " + x)

# myfunc()

# print("Python is " + x)


# Also, use the global keyword if you want to change a global variable inside a function.

# Example
# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"
print("Python is " + x)

def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)
  

myfunc()

print("Python is " + x)
