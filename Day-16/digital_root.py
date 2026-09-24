# Repeatedly Add digits until a single digit remains.
def digital_root(num):
    while num >= 10:
        sum = 0

        while num > 0:
            dgt = num % 10
            sum = sum + dgt
            num = num // 10

        num = sum

    return num

print(digital_root(9875))
print(digital_root(1234))
