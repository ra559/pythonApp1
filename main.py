numb1 = int(input("Enter number: "))
numb2 = int(input("Enter another number: "))

def addition(numb1, numb2):
    result = numb1 + numb2
    return result


def subtraction(numb1, numb2):
    if numb1 > numb2:
        bigger = numb1
        smaller = numb2
    else:
        bigger = numb2
        smaller = numb1
    result = bigger - smaller
    return result


def multiplacation(numb1, numb2):
    result = numb1 * numb2
    return result


def division(numb1, numb2):
    if numb1 > numb2:
        bigger = numb1
        smaller = numb2
    else:
        bigger = numb2
        smaller = numb1
    result = bigger / smaller
    return result


print("The addition of ", numb1, "and", numb2, "is", addition(numb1, numb2))
print("The subtraction of ", numb1, "and", numb2, "is", subtraction(numb1, numb2))
print("The multiplication of ", numb1, "and", numb2, "is", multiplacation(numb1, numb2))
print("The division of ", numb1, "and", numb2, "is", division(numb1, numb2))
