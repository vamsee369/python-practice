balance = int(input("Enter balance: "))
withdrawal = int(input("Enter withdrawal: "))

if withdrawal > balance:
    raise Exception("Error: Insufficient balance.")
else:
    print("Transaction successful.")
