# reverse
string = input("enter a string : ")
reverse_string = string[::-1]
print(reverse_string)

# vowels count
string = input("enter a string :")
string = string.lower()
vowels = ("aeiou")
count = 0
for char in string:
    if char in vowels:
        count += 1
print(count)

# upper and lower case convert
string = input("enter a string : ")
lower = string.lower()
upper = string.upper()
print(lower)
print(upper)
