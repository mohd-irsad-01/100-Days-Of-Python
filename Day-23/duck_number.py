# Check whether a number is a Duck Number.
def is_duck_number(num):
    num_str = str(num)
    
    # A Duck Number should not start with '0' and should contain at least one '0'
    if num_str[0] == '0':
        return f"{num} is not a Duck Number because it starts with 0."
    if '0' in num_str:
        return f"{num} is a Duck Number."
    return f"{num} is not a Duck Number."
print(is_duck_number("123"))  # Output: 123 is not a Duck Number.
print(is_duck_number("1023"))  # Output: 1023 is a Duck Number.
