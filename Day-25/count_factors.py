# Print all Factors of a Number.
def print_factors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=", ")
    print()  # For a new line after printing all factors.
print_factors(12)  # Output: 1, 2, 3, 4, 6, 12


# Count the Number of Factors of a Number.
def count_factors(num):

    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return f"{num} has {count} factors."

print(count_factors(12))  # Output: 12 has 6 factors.
