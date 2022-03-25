# This is Michael Jordan. He is 35 years old. He is a programmer.
# This is John Rosales. He is 20 years old. He is a student.
# This is Mark Guillen. He is 30 years old. He is a doctor.
# This is KB Tonel. He is 27 years old. He is an engineer.

users = [
    {
        'first_name': 'Michael',
        'last_name': 'Jordan',
        'age': 35,
        'profession': 'programmer'
    },
    {
        'first_name': 'John',
        'last_name': 'Rosales',
        'age': 20,
        'profession': 'student'
    },
    {
        'first_name': 'KB',
        'last_name': 'Tonel',
        'age': 27,
        'profession': 'engineer'
    },
    {
        'first_name': 'Mark',
        'last_name': 'Guillen',
        'age': 30,
        'profession': 'doctor'
    },
]

# vowels = ["a", "e", "i", "o", "u"]
# for user in users:
#     profession_article = "a"
#     if user["profession"][0] in vowels:
#         profession_article = "an"
#     print("This is {firstName} {lastName}. He is {age} years old. He is {article} {profession}.".format(
#         lastName=user["last_name"], article=profession_article, firstName=user["first_name"], profession=user["profession"], age=user["age"]))

n = 45
if n > 30:
    print("Old")
else:
    print("Young")