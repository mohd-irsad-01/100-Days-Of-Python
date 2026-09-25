# Find sum of squares of digits

def sum_of_squares(num):

    sum = 0
    while num > 0:
        dgt = num % 10
        sum = sum + dgt * dgt
        num = num // 10

    return sum

print(sum_of_squares(123))
print(sum_of_squares(32))
