# Reverse a String.
def reverse_string(s):
    return s[::-1]

s = input("Enter String: ")
print(reverse_string(s))



# Check if String is Palindrome.
def check_palindrome(s):
    if s == s[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

s = input("Enter String: ")
print(check_palindrome(s))
