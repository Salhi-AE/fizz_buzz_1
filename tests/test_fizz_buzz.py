from src.fizz_buzz import fizz__buzz

def test_function_is_return_fizz():
    assert fizz__buzz(3)=="fizz"

def test_function_is_return_0():
    assert fizz__buzz(5)=="buzz"
