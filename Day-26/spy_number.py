# Check whether a number is spy number.
def is_spy_number(num):
    temp = num
    sum = 0
    product = 1
    while temp > 0:
        digit = temp % 10
        sum = sum + digit
        product = product * digit
        temp = temp // 10
    if sum == product:
        return "Spy Number"
    return "Not a spy number"
print(is_spy_number(1124))  # Output: Spy number
print(is_spy_number(124))   # output: Not a spy number
