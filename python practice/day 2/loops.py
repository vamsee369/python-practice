# numbers from 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# Sum of all even numbers from 1 to 100
total = 0
for i in range(2, 100, 2):
    total += i
print(total)

# Countdown using a while loop(10sec)
count = 11
while count > 0:
    count -= 1
    print(count)
print("count down completed .")
