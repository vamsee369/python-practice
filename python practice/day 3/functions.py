# prime
def prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5)+1):
        if number % i == 0:
            return False
    return True


number = int(input(" enter a number : "))
print("prime" if prime(number) else "not prime")


# factorial
def factorial(number):
    result = 1
    for i in range(2, number+1):
        result *= i
    return result


number = int(input("enter a number : "))
print(factorial(number))

# largest number


def largest_in_list(numbers):
    return max(numbers)


nums = [10, 50, 20, 70, 30]
print("Largest number:", largest_in_list(nums))
# finish
