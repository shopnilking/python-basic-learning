# Python Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword:

# def my_function():
#     print("Hello from a function")

# Calling a Function
# To call a function, use the function name followed by parenthesis:

# def my_function():
#     print("Hello from a function")

# my_function()

# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

# def my_function(name):
#     print("Hello " + name + ". How are you?")


# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

# def fullName(fname, lname):
#     print(fname + " " + lname)


# fullName("Md Shahin", "Howlader")
# fullName("Md Saiful", "Howlader")


# def userInfo(fname, lname, age):
#     print("User full name : "+fname + " " + lname + ". He/She is " + str(age) + " years old.")

# userInfo("Md", "Shahin", "30")
# userInfo("Md", "Saiful", "20")

# def fullName(fname, lname):
#     return fname + " " + lname


# fullName = fullName("Md", "Shahin")
# print(fullName)

# If you try to call the function with 1 or 3 arguments, you will get an error:
# Example
# This function expects 2 arguments, but gets only 1:

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Emil")

# def my_function(fname="", lname=""):
#     print(fname + " " + lname)


# # my_function("Emil")
# my_function()

# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# def foods(food):
#     for x in food:
#         print(x)


# fruits = ["apple", "banana", "cherry"]
# foods(fruits)

# Return Values
# To let a function return a value, use the return statement:

# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

# Example
# def myfunction():
#   pass


# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

def reduceFun(n):
    if(n < 1):
        return 0
    print(n)
    return reduceFun(n-1)


reduceFun(10)