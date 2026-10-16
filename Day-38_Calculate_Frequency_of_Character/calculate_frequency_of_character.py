# Q. Calculate Frequency of Characters

text = input("Enter string: ")

freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)

# Ex: hello -> {'h':1, 'e':1, 'l':2, 'o':1}
