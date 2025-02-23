class Calculator:#Defines a Calculator class that takes two numbers (num1, num2) as input.
    def __init__(self, num1, num2):#__init__ is the constructor that initializes num1 and num2 when a Calculator object is created.
        self.num1 = num1
        self.num2 = num2

    def add(self):#Returns the sum of num1 and num2.
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 == 0:
            return "Error: Cannot divide by zero" #Handles division by zero: If num2 is 0, it returns an error message instead of crashing.
        return self.num1 / self.num2

# User input 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

calculator = Calculator(num1, num2)

print("Select operation: +, -, *, /")
operator = input("Enter operation: ")

operations = { #A dictionary (operations) maps the chosen operator (+, -, *, /) to the corresponding method in the Calculator class.
             #   This makes the code cleaner and avoids multiple if-elif conditions.
    "+": calculator.add,
    "-": calculator.subtract,
    "*": calculator.multiply,
    "/": calculator.divide
}

print("Result:", operations.get(operator, lambda: "Invalid operator")())#get(operator) retrieves the corresponding function from the dictionary.
                                                                  #  If the operator is invalid (not in the dictionary), it returns "Invalid operator".


