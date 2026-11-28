# Oringinal list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1. Get even numbres
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)

# 2.Get squares of numbers
squares = [x ** 2 for x in numbers]
print("Squares:", squares)

# 3. Numbers greater than 5
greater_numbers = [x for x in numbers if x > 5]
print("Numbers Greater Than 5:", greater_numbers)

# 4. Names into uppercase
names = ["irsad", "irfan", "sandeep"]
upper_name = [name.upper() for name in names]
print("Uppercase Names:", upper_name)
