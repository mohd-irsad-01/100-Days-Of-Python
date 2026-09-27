# Check whether a number is strong number or not.
def is_strong(num):
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        fact = 1
        for i in range(1, digit + 1):
            fact = fact * i
        sum = sum + fact
        num = num // 10
    if sum == temp:
        return f"{temp} is Strong number"
    else:
        return f"{temp} is Not Strong number"
    
print(is_strong(145))
print(is_strong(123))
