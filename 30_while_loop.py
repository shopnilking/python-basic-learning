# Python While Loops

# i = 1
# while i < 6:
#   print(i)
#   i += 1

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# The continue Statement
# With the continue statement we can stop the current iteration, and continue with the next:

i = 0
while i < 6:
  
  i += 1
  print(i)
  if i == 3:
      continue


# The else Statement
# With the else statement we can run a block of code once when the condition no longer is true:

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("Loop is finished")
