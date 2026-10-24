s = input("Enter a string: ")

count = 0
in_word = False

for ch in s:
    if ch != ' ' and ch != '\t' and ch != '\n':
        if not in_word:
            count += 1
            in_word = True
    else:
        in_word = False

print("Number of words: ", count)
