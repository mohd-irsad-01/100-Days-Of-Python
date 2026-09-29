# Check Automorphic Number.
def is_automorphic(num):
    orig = num
    sqr = num * num
    power = 10
    while num > 0:
        if sqr % power != orig % power:
            return f"{orig} is Not Automorphic number"
        num = num // 10
        power = power * 10
    return f"{orig} is Automorphic number"

print(is_automorphic(25))   # Automorphic number
print(is_automorphic(13))   # Not Automorphic number
