# Q. Remove Characters Except Alphabets.

text = input("Enter string: ")


result = ""

for ch in text:
    if ch.isalpha():
        result += ch

print(f"Only alphabets: {result}")

# Ex: Hello@12!  ->  Hello
