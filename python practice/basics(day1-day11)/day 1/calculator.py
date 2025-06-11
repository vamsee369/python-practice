def add(x, y):
    return (x+y)


def subtract(x, y):
    return (x-y)


def multiply(x, y):
    return (x*y)


def divison(x, y):
    if y != 0:
        return (x/y)
    else:
        print("can not be divideed with zero (0)  ")


print("choose an option")
print("1 for adition :")
print("2 for subtraction :")
print("3 for multiplication : ")
print("4 for divison : ")
choice = input("what is your choice ")
num1 = float(input("enter first number : "))
num2 = float(input("enter second number : "))
if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiply(num1, num2)
elif choice == '4':
    result = divison(num1, num2)
else:
    print("an error occured check once. ")
print("the result is : ", result)
# finish
