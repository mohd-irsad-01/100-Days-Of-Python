octal = int(input("Enter an octal number: "))

decimal = 0
power = 0

while octal > 0:
    digit = octal % 10
    decimal = decimal + digit * (8 ** power)
    octal = octal // 10
    power = power + 1
    
print("Decimal number: ", decimal)
