# Q. Change every letter to the next alphabet.
s = input("Enter a string: ")

result = ""

for ch in s:
    if ch == 'z':
        result += 'a'
    elif ch == 'Z':
        result += 'A'
    elif ch.isalpha():
        result += chr(ord(ch) + 1)
    else:
        result += ch

print(result)
