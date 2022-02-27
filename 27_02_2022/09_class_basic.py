class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y


x = int(input("value of x"))
y = int(input("value of y"))

calculator = Calculator(x, y)
print(calculator.add())
print(calculator.sub())
print(calculator.mul())
print(calculator.div())
