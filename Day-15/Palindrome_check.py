# Check whether a number is a palindrome or not

def is_palindrome(num):
    temp = num
    reverse = 0

    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num // 10

    if temp == reverse:
        return "Palindrome number"
    else:
        return "Not a palindrome number"
    
print(is_palindrome(131))  # Palindrome number
print(is_palindrome(123))  # Not a palindrome number
