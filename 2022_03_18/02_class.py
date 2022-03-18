class User:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


    def fullName(self):
        # Saiful Islam
        return self.firstName + " " + self.lastName

    def greetings(self):
        # Hello, Saiful Islam
        return "Hello " + self.fullName()

    def sayGoodBye(self):
        # Good bye, Saiful Islam
        return "GoodBye! " + self.fullName()

    def age(self, age):
        # Saiful Islam is 22 years old
        return self.fullName() + " is " + str(age) + " years old."


user = User("Saiful", "Islam")
fullName = user.fullName()
greetings = user.greetings()
sayGoodBye = user.sayGoodBye()
age = user.age(22)
print(fullName)
print(greetings)
print(sayGoodBye)
print(age)
