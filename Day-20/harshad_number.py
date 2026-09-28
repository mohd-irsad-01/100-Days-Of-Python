# Check Harshad Number
def is_harshad(num):
    temp = num
    sum = 0
    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10
    if  temp % sum == 0:
        return f"{temp} Harshad number"
    else:
        return f"{temp} is Not Harshad number"

print(is_harshad(18))  # Harshad number
print(is_harshad(13))  # Not Harshad number
