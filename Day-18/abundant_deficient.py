# Check Abundant Number.
def is_abundant(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    if sum > num:
        return f"{num} is Abundant"
    else:
        return f"{num} is Not Abundant"


# Check Deficient Number.
def is_deficient(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    if sum < num:
        return f"{num} is Deficient"
    else:
        return f"{num} is Not Deficient"

# Function Call
print(is_abundant(12))      # Abundant Number
print(is_abundant(8))       # Not Abundant Number

print(is_deficient(8))      # Deficient Number
print(is_deficient(12))     # Not Deficient Number
