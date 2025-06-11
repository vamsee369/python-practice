try:
    guess = int(input("Guess a number (1-10): "))
    if 1 <= guess <= 10:
        print("Good guess!")
    else:
        print("Out of range.")
except ValueError:
    print("Please enter a number between 1 and 10.")
