number = input("enter a number : ")
if number == '0':
    print("the number is zero")
elif number < '0':
    print("the number is a negative number")
else:
    print("the number is a postive number")

total = 0
for i in range(2, 101, 2):  # start at 2, step by 2
    total += i

print("Sum of even numbers from 1 to 100 is:", total)
