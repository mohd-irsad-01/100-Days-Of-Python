# Check whether a number is prime or not

def is_prime(n):
    count = 0

    for i in range(1, n+1):
        if n % i == 0:
            count += 1

    if count == 2:
        return "Prime number"
    else:
        return "Not a prime number"

print(is_prime(7))    # Prime number
print(is_prime(10))   # Not a prime number
