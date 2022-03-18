class Parent:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def fullName(self):
        return self.firstname + " " + self.lastname

class Child(Parent):

    def age(self, age):
        return age

    def greetings(self):
        return "Hello! " + super().fullName()

x = Child("Saiful", "Islam")
print(x.fullName())
print(x.age(22))
print(x.greetings())
