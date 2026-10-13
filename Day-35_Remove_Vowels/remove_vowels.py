# Q. Remove All Vowels from a String.
text = input("Enter string: ")

vowels = "aeiouAEIOU"

result = ""

for ch in text:
    if ch not in vowels:
        result += ch

print(f"Without vowels: {result}")
