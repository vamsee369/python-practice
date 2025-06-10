age = int(input("Enter age: "))
if age < 0 or age > 150:
    raise ValueError("Error: Invalid age.")
else:
    print("Age accepted.")
