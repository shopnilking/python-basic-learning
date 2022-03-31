text = "{'first_name': 'Michael','last_name': 'Jordan','age': '35','profession': 'programmer'},{'first_name': 'John','last_name': 'Rosales','age': '20','profession': 'student'},{'first_name': 'KB','last_name': 'Tonel','age': '27','profession': 'engineer'},{'first_name': 'Mark','last_name': 'Guillen','age': '30','profession': 'doctor'}"
# need to make a list of ages
# ages = ['35', '20', '27', '30']

# list1 = text.split(',')
# ageList = []
# for x in list1:
#     if x.startswith("'age': '"):
#         ageList.append(int(x[8:-1]))
# print(ageList)


list2 = text.split(',')
firstNameList = []
for x in list2:
    if x.startswith("{'first_name': '"):
        firstNameList.append(x[16:-1])
# print(firstNameList)


list3 = text.split(',')
lastNameList = []
for x in list3:
    if x.startswith("'last_name': '"):
        lastNameList.append(x[14:-1])
# print(lastNameList)


# list4 = text.split(',')
# fullNameList = []
# for x in list4:
#     if x.startswith("{'first_name': '"):
#         firstName = x[16:-1]
#     if x.startswith("'last_name': '"):
#         lastName = x[14:-1]
#         fullNameList.append(firstName + " " + lastName)

# print(fullNameList)

# fullNameList = []
# for (x, y) in zip(firstNameList, lastNameList):
#     fullNameList.append(x + " " + y)
# print(fullNameList)

fullNameList = []
for x in range(len(firstNameList)):
    fullNameList.append(firstNameList[x] + " " + lastNameList[x])


# hw
# 1. Create a list of first names
# 2. Create a list of last names
# 3. Create a list of full names
