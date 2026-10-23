# Q. Change case of each character.

s = input("Enter a string: ")

result = ""

for ch in s:
    if ch.islower():
        result += ch.upper()
    elif ch.isupper():
        result += ch.lower()
    else:
        result += ch

print("Changed string: ", result)
