from unittest_1.calculator import Calculator, CalculatorError
import pytest, mock

def test_Calculator_add():
  calculator = Calculator()
  result = calculator.add(4, 2)
  assert result == 6

def test_weird_add():
  calculator = Calculator()

  with pytest.raises(CalculatorError) as context:
    result = calculator.add(4, "two")  

  assert str(context.value) == "\"two\" was not a number"

def test_weirder_add():
  calculator = Calculator()

  with pytest.raises(CalculatorError) as context:
    result = calculator.add("four", "two")  
  
  assert str(context.value) == "\"four\" was not a number"

def test_Calculator_substract():
  calculator = Calculator()
  result = calculator.substract(9, 3)
  assert result == 6

def test_Calculator_multiply():
  calculator = Calculator()
  result = calculator.multiply(9, 3)
  assert result == 27

def test_Calculator_divide():
  calculator = Calculator()
  result = calculator.divide(9, 3)
  assert result == 3 

def test_Calculator_divide_by_zero():
  calculator = Calculator()
  with pytest.raises(CalculatorError):
    result = calculator.divide(9, 0)

# def test_init():
#   from unittest_1 import calculator
#   with mock.patch.object(calculator, 'main', return_value=42):
#     with mock.patch.object(calculator, '__name__', '__main__'):
#       with mock.patch.object(calculator.sys,'exit') as mock_exit:
#         calculator.init()    
             
#         assert mock_exit.call_args[0][0] == 42