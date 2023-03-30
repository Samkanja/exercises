def math_arithmetic(a, b):
    sum_ab = a + b
    diff = a - b
    prod = a * b
    quotient  = a // b
    rem = a % b
    return sum_ab, diff, prod , quotient, rem

a , b = map(int, input('a and b : ').split())
print(math_arithmetic(a,b))