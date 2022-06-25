from unittest import result
from unittest_1.math_func import add, product, div

def test_add():
  assert add(7,3) == 10
  assert add(7) == 9

def test_product():
  assert product(5, 5) == 25
  assert product(5) == 10

def test_add_strings():
  result = add('Hello', ' World')
  assert result == 'Hello World'

  assert type(result) == str
  assert 'Hello' in result

def test_product_strings():
  assert product('Hello ', 3) == 'Hello Hello Hello '
  
  result = product('Hello ')
  assert result == 'Hello Hello '
  
  assert type(result) == str
  assert 'Hello ' in result

def test_divide():
  assert div(5, 2) == 2.5
