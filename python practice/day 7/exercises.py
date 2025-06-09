# Recursive Factorial
from functools import reduce


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)


print(factorial(10))

# Average Using args


def average(*numbers):
    total = sum(numbers)
    num = len(numbers)
    avg = total/num
    return avg


print(average(1, 2, 3, 4))
# Convert List to Uppercase Using map()
lists = ["vamsee", "hello", "world"]
uppered = list(map(lambda word: word.upper(), lists))
print(uppered)

# Filter Odd Numbers Using filter()
num = [1, 2, 3, 4, 5, 6]
odd = list(filter(lambda x: x % 2 != 0, num))
print(odd)

# Product of List Using reduce()
num = [1, 2, 3, 4]
product = reduce(lambda x, y: x*y, num)
print(product)


# Cube Using Lambda
def cube(x): return x*x*x


print(cube(2))
# Apply Function Twice


def apply_twice(func, value):
    r_1 = func(value)
    r_2 = func(r_1)
    return r_2


print(apply_twice(lambda x: x + 2, 5))
