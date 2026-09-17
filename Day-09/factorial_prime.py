# 1. Factorial Functions
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


# 2. Check Prime Number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# Function calls
print(f"Factorial of 5 is {factorial(5)}")
print(f"Factorial of 6 is {factorial(6)}")

print(is_prime(7))       # True
print(is_prime(10))      # False
