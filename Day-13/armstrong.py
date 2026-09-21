# Check whether a number is an Armstrong number
def is_armstrong(n):
    original = n
    total = 0
    digits = len(str(n))

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10
    if total == original:
        return True
    else:
        return False

print(is_armstrong(153))   # True
print(is_armstrong(370))   # True
print(is_armstrong(133))   # False
