# Find the GCD of an Array of Numbers.
def find_gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a
def gcd_of_array(arr):
    i = 0
    result = arr[0]
    while i < len(arr):
        result = find_gcd(result, arr[i])
        i = i + 1
    return result

print(gcd_of_array([12, 18, 24]))  # Output: 6
print(gcd_of_array([7, 14, 21]))  # Output: 7
