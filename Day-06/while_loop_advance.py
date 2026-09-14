# (Question-1) -  Reverse a number
num = int(input("Enter number to reverse: "))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10
print(f"Reverse: {rev}")


# (Question-2) - Find the sum of digits of a given number
num = int(input("Enter a number: "))
total = 0
while num > 0:
    digit = num % 10
    total = total + digit
    num = num // 10
print(f"Sun of digits is {total}")
