octal = int(input("Enter an octal: "))
decimal = 0
power = 0
while octal > 0:
    digit = octal % 10
    decimal = decimal + digit * (8 ** power)
    octal = octal // 10
    power = power + 1

binary = 0
power = 0
while decimal > 0:
    remainder = decimal % 2
    binary = binary + remainder * (10 ** power)
    decimal = decimal // 2
    power = power + 1

print("Binary number: ", binary)
