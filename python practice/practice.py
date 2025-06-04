# even or odd
# +
# number = input("give me any number which you want")
# check = int(number) % 2
# if int(check == 1):
# print("the the number is odd")
# else:
# print("the number is even")


# Check if a string is a palindrome
# text = input("enter any word of your choice  ")
# reverse_opperation = ""
# for char in text:
# reverse_opperation = char + reverse_opperation
# if text == reverse_opperation:
# print("the word is a palindrome")
# else:
#  print("the word is not a palindrome")
# Check if a string is a palindrome
# text = input("give me a word of your choice : ")
# if text == text[::-1]:
#   print("the word is palindrome ")
# else:
# print("the word is not a palindrome ")

# largest of three numbers entered


# largest of three numbers entered
# number_1 = float(input("give number 1 : "))
# number_2 = float(input("give number 2 : "))
# number_3 = float(input("give number 3 : "))
# if number_1 >= number_2 and number_3:
#   print("greater of the among numbers is ", number_1)
# elif number_2 >= number_1 and number_3:
#   print("greater of the among numbers is ", number_2)
# else:
#   print("the greater of the among numbers is ", number_3)

# multiplication table of a number entered by the user
# number = float(input("the multiplicative number is : "))
# print(f"the multiplication table for {number} is : ")

# for v in range(1, 11):
#  print(f"{number} * {v} = {number * v} ")


# the sum of all numbers from 1 to n, where n is given by the user.
# number = int(input("give the value for n : "))
# total = 0
# for v in range(1, number+1):
#   total += v
# print(f"the sum of all numbers from 1 to {number} is : {total}")

# number = int(input("enter a number : "))
# factorial = 1
# if number < 0:
#   print("the factorial is not defined for negative numbers")
# elif number == 0:
#   print("the factorial of 0 is 1")
# else:
#   for v in range(1, number + 1):
#      factorial *= v
# print(f"the valus of factorial of {number} is {factorial}")


# num = int(input("Enter a number: "))

# if num <= 1:
#   print("Not a prime number.")
# else:
#   is_prime = True

#  for i in range(2, int(num ** 0.5) + 1):
#     if num % i == 0:
#        is_prime = False
#       break

# if is_prime:
#   print(f"{num} is a prime number.")
# else:
#   print(f"{num} is not a prime number.")


# print("Prime numbers between 1 and 100 are:")

# for num in range(2, 101):
# is_prime = True
# for i in range(2, int(num ** 0.5) + 1):
# if num % i == 0:
# is_prime = False
# break

# if is_prime:
#    print(num, end=" ")


import string
text = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print(f"Number of vowels in the string: {count}")


num = int(input("Enter a number: "))

num_str = str(num)
num_digits = len(num_str)

sum_of_powers = 0
for digit in num_str:
    sum_of_powers += int(digit) ** num_digits

if sum_of_powers == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")


def pangram(sentence):
    sentence = sentence.lower()
    alphabets = set(string.ascii_lowercase)
    sentence_letters = set(filter(str.isalpha, sentence))
    return alphabets.issubset(sentence_letters)


print(pangram(" "))


def pangram(sentence):
    sentence = sentence.lower()
    alphabets = set(string.ascii_lowercase)
    sentence_letters = set(filter(str.isalpha, sentence))
    missing = alphabets - sentence_letters
    if not missing:
        result = "pangram"
    else:
        result = ("not a pangram, missing letters is/are :" +
                  ",".join(sorted(missing)))
        print(result)
        return (result)


pangram(" ")


def number_frequency(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    print(frequency)
    return (frequency)


number_frequency("is am is am is am")


def is_palindrome(word):

    word = word.lower()

    reversed_word = word[::-1]

    if word == reversed_word:
        print("✅ Palindrome")
        return True
    else:
        print("❌ Not a palindrome")
        return False


is_palindrome(" ")


def even_number(numbers):
    required_numbers = []
    for number in numbers:
        if number % 2 == 0:
            required_numbers.append(number)
    print(required_numbers)
    return (required_numbers)


even_number([1, 2, 3, 4, 5, ])


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_sum(n):
    total = 0
    for i in range(1, n + 1):
        total += factorial(i)
    return total


def count_vowels(text):
    text = text.lower()
    vowels = ("aeiou")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print(count)
    return (count)


def second_largest(numbers):
    number = list(set(numbers))
    number.sort(reverse=True)
    result = number[1]
    print(result)
    return (result)


second_largest([1, 2, 3, 4, 5])


def tupels(list_of_tupels):
    return sorted(list_of_tupels, key=lambda x: x[1])


print(tupels([(2, 1), (4, 2), (1, 3)]))


def add(x, y):
    return x+y


def subtract(x, y):
    return x-y


def multiplication(x, y):
    return x*y


def divison(x, y):
    if y != 0:
        return x/y
    else:
        return ("error can not be divisible by zero")


print("press 1 for addition ")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for divison")
choice = input("select operation :  ")
num1 = float(input("your first number is : "))
num2 = float(input("your second number is : "))

if choice == '1':
    result = add(num1, num2)
elif choice == '2':
    result = subtract(num1, num2)
elif choice == '3':
    result = multiplication(num1, num2)
elif choice == '4':
    result = divison(num1, num2)
else:
    result = "invalid input"
print("result is : ", result)
