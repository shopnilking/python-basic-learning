# This is Michael Jordan. He is 35 years old. He is a programmer.
# This is John Rosales. He is 20 years old. He is a student.
# This is Mark Guillen. He is 30 years old. He is a doctor.
# This is KB Tonel. He is 27 years old. He is an engineer.

users = [
    {
        'first_name': 'Michael',
        'last_name': 'Jordan',
        'age': '35',
        'profession': 'programmer'
    },
    {
        'first_name': 'John',
        'last_name': 'Rosales',
        'age': '20',
        'profession': 'student'
    },
    {
        'first_name': 'Mark',
        'last_name': 'Guillen',
        'age': '30',
        'profession': 'doctor'
    },
    {
        'first_name': 'KB',
        'last_name': 'Tonel',
        'age': '27',
        'profession': 'engineer'
    },
]

vowels = ['a', 'e', 'i', 'o', 'u']
profession_article = 'a'
for user in users:
    if user['profession'][0] in vowels:
        profession_article = 'an'

    print("This is {} {}. He is {} years old. He is {} {}.".format(
        user['first_name'], user['last_name'], user['age'], profession_article, user['profession']))
