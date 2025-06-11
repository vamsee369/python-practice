num = int(input("Enter a number to see its multiplication table: "))

print(f"Multiplication Table for {num} is:")
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
