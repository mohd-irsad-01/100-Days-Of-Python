def bunary_to_decimal(binary):
    
    decimal = 0
    power = 0

    while binary > 0:
        digit = binary % 10
        decimal = decimal + digit * (2 ** power)
        binary = binary // 10
        power = power + 1
    return decimal

print(bunary_to_decimal(1011))
print(bunary_to_decimal(1100))
print(bunary_to_decimal(101))
