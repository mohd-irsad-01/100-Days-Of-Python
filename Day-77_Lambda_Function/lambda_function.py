# 1. Add two numbers
add = lambda a, b: a + b
print("Addition:", add(10, 20))

# 2. Square
square = lambda n: n * n
print("Square:", square(5))

# 3. Largest number
largest = lambda a, b: a if a > b else b
print("Largest Number:", largest(15, 25))

# 4. Even or Odd
check = lambda n: "Even" if n % 2 == 0 else "Odd"
print("Number check:", check(8))

# 5. Cube
cube = lambda n: n ** 3
print("Cube:", cube(4))

# 6. Simple Interest
interest = lambda p, r, t: (p * r * t) / 100
print("Simple Interest:", interest(5000, 5, 2))
