text = input("Enter a string: ")

digits = 0
letters = 0
special = 0

for ch in text:
    if ch.isdigit():
        digits += 1
    elif ch.isalpha():
        letters += 1
    else:
        special += 1

print("Digits: ", digits)
print("Letters: ", letters)
print("Special Characters: ", special)
