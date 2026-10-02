# Check whether a number is a happy number or not.
n = int(input("Enter a number: "))
while n != 1 and n  != 4:
    sum = 0

    while n > 0:
            digit = n % 10
            sum = sum + digit * digit
            n = n // 10

    n = sum

if n == 1:
    print("Happy Number")
else:
    print("Not a Happy Number")
