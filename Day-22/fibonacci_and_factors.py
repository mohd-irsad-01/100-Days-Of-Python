# Print the Fibonacci Series.
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

fibonacci(10)   # Output: 0 1 1 2 3 5 8 13 21 34



# Count the Number of Factor of a number.
def factor(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
        return f"{num} has {count} factors"
    
print(factor(12))   # Outout: 12 has 6 factors
