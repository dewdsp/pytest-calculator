import numbers
import sys

class CalculatorError(Exception):
  """An exception class for Calculator"""

class Calculator:

  def add(self, x, y):
    self._validate_operand(x)
    self._validate_operand(y)
    return x + y

  def substract(self, x ,y):
    self._validate_operand(x)
    self._validate_operand(y)
    return x - y

  def multiply(self, x, y):
    self._validate_operand(x)
    self._validate_operand(y)
    return x * y

  def divide(self, x, y):
    self._validate_operand(x)
    self._validate_operand(y)
    try:
      return x / y
    except ZeroDivisionError: 
      raise CalculatorError("Can't divide by zero")

  def _validate_operand(self, operand):
    if not isinstance(operand, numbers.Number):
      raise CalculatorError(f'"{operand}" was not a number')

if __name__ == '__main__':
  print("Let's calculate")
  calculator = Calculator()
  operations = [
    calculator.add,
    calculator.substract,
    calculator.multiply,
    calculator.divide,
  ]
  while True:
    print("Pick an operation")
    for i, operation in enumerate(operations, start=1):
      print(f"{i}: {operation.__name__}")
    print("q: quit")
    operation = input("Pick an operation: ")
    if operation == 'q':
      sys.exit()
    op = int(operation)
    x = float(input("Enter the first number: "))
    y = float(input("Enter the first number: "))

    try:
      print(f"Output is: {operations[op -1](x, y)}")
    except CalculatorError as ex:
      print(ex)
    except IndexError as ex:
      print(ex)