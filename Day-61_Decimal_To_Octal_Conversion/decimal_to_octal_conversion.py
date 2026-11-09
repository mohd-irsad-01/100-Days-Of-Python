decimal = int(input("Enter a decimal number: "))
octal = 0
power = 0
while decimal > 0:
    remainder = decimal % 8
    octal = octal + remainder * (10 ** power)
    decimal = decimal // 8
    power = power + 1
print("octal number:", octal)
