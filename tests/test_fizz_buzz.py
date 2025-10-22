from src.fizz_buzz import fizz__buzz

def test_function_is_return_fizz():
    assert fizz__buzz(3)=="fizz"

def test_function_is_return_0():
    assert fizz__buzz(5)=="buzz"

def test_function_is_return_8():
    assert fizz__buzz(8) == 8

def test_function_is_return_the_10():
    assert fizz__buzz(10) == 10