from functools import reduce

# 1. Filter enen numbers
numbers = [10, 15, 20, 25, 30]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers: ",even_numbers)

# 2. Map sqaure of numbers
numbers = [2, 3, 4, 5]
sqaures = list(map(lambda x: x ** 2, numbers))
print("Squars:", sqaures)

# 3. Reduce sum of numbers
numbers = [10, 20, 30, 40]
total = reduce(lambda x, y: x + y, numbers)
print("Total Sum:", total)
