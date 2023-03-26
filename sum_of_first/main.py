def sum_first_int(n):
    """sum = ((n)(n + 1))/2"""
    if n < 1:
        return  -1
    
    return ((n)*(n + 1))/2

n = int(input('num: '))
print(sum_first_int(n))