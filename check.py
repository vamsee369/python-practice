# Write a function to check if a string is a pangram.✅

# Take a list of numbers and return a new list with only even numbers.✅

# Create a function that returns the factorial of a number.✅

# Count the number of vowels in a string.✅

# Find the second largest number in a list.✅

# Create a simple calculator using functions.✅

# Write a program that reads a file and prints its contents.

# Count word frequency in a sentence using a dictionary.✅

# Sort a list of tuples based on the second value.✅

# Create a menu-driven program (like a small app with choices).

# This program reads and prints the contents of a file named "example.txt"

def read_file():
    try:
        # Open the file in read mode
        with open("example.txt", "r") as file:
            # Read the contents of the file
            content = file.read()

            # Print the file content
            print("File Contents:\n")
            print(content)

    except FileNotFoundError:
        print("Error: The file 'example.txt' was not found.")


# Call the function
read_file()
