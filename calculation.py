

def add(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

def sub(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = result - number
    return result

def mul(numbers):
    result = 1
    for number in numbers:
        result = result * number
    return result

def div(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        if number == 0:
            return False
        result = result / number
    return result

def mod(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        if number == 0:
            return False
        result = result % number
    return result