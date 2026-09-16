# 1. Simple function
def greet():
    print("Hello Welcome to Python")

# 2. Function with parameter
def greet_user(name):
    print(f"Hello, {name}")

# 3. Function with return value
def add(a, b):
    return a + b

# 4. Function to check even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Calling functions
greet()
greet_user("Mohd Irsad")
result = add(4, 5)
print(f"Sum is: {result}")
print(check_even_odd(7))
print(check_even_odd(10))
