def binary_to_octal(binary):
    decimal = 0
    octal = 0
    power = 0

    while binary > 0:
        digit = binary % 10
        decimal = decimal + digit * (2 ** power)
        binary = binary // 10
        power = power + 1
    
    power = 0
    while decimal > 0:
        digit = decimal % 8
        octal = octal + digit * (10 ** power)
        decimal = decimal // 8
        power = power + 1

    return octal

print(binary_to_octal(11111))
print(binary_to_octal(1100110))
print(binary_to_octal(100))
