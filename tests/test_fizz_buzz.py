from src.fizz_buzz import fizz__buzz

def test_function_is_return_fizz():
    assert fizz__buzz(3)=="fizz"

def test_function_is_return_buzz():
    assert fizz__buzz(5)=="buzz"

def test_function_is_return_buzz_num_9():
    assert fizz__buzz(9)=="fizz"