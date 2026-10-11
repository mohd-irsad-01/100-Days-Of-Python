# Q. Count Vowels, Consonants and Spaces in a String.

text = input("Enter string: ")

vowel = 0
consonents = 0
space = 0

v = "aeiouAEIOU"
for ch in text:
    if ch in v:
        vowel += 1

    elif ch == ' ':
        space += 1

    elif ch.isalpha():
        consonents += 1

print(f"Vowels: {vowel}")
print(f"Consonents: {consonents}")
print(f"Spaces: {space}")
