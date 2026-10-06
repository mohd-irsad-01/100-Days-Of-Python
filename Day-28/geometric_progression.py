# Find Sum of a Geometric Progression.
def gp_sum(a, r, n):

    i = 0
    sum = 0
    term = a
    while i < n:
        sum = sum + term
        term = term * r
        i = i + 1
    return sum

print(gp_sum(2, 3, 4))  #Output: 80
print(gp_sum(1, 2, 5))  #Output: 31
