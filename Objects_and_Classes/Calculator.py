class Calculator:
  def __init__(self,num1 = 0,num2=0):
    self.num1 = num1
    self.num2 = num2
  def add(self):
    return self.num1 + self.num2
  def subtract(self):
    return self.num1 - self.num2
  def multiply(self):
    return self.num1 * self.num2
  def divide(self):
    if self.num2 != 0:
      return self.num1 / self.num2
    else:
      return 'Error! Division by zero '
#Tests
print("Calculator")
Num1 = int(input("Number one: "))
Num2 = int(input("Number two: "))
Numbers = Calculator(Num1,Num2)
operation = input("Choose an operation +,-,*,/: ")
if operation == '+':
  result = Numbers.add()
elif operation == '-':
  result = Numbers.subtract()
elif operation == '*':
  result = Numbers.multiply()
elif operation == '/':
  result = Numbers.divide()

print(f"{Num1} {operation} {Num2} = {result}") 
