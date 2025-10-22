def fizz__buzz(num:int) -> str | int:

    if num % 3 == 0:
        return "fizz"
    if num % 5 == 0:
        return "buzz"
    if num % 3 and num % 5 == 0:
        return "fizzbuzz"
    return num