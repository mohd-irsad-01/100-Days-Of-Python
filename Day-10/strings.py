# 1. Palindrome Checker
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

# 2. Count Vowels
def count_vowel(s):
    vowel = "AEIOUaeiou"
    count = 0
    for i in s:
        if i in vowel:
            count += 1
    return count

# 3. Word Counter
def word_counter(s):
    return len(s.split())



# Function calls
print(is_palindrome("naman"))
print(count_vowel("Python Programming"))
print(word_counter("I am learning Python"))
