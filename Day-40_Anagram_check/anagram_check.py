# Q. Check if two strings are Anagrams.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if sorted(str1) == sorted(str2):
    print("Strings are Anagrams")
else:
    print("Strings are not Anagrams")
