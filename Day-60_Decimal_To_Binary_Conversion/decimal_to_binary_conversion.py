def decimal_to_binary(decimal):
    binary = 0
    power = 0
    while decimal > 0:
        digit = decimal % 2
        binary = binary + digit * (10 ** power)
        decimal = decimal // 2
        power = power + 1
    return binary
print(decimal_to_binary(18))
