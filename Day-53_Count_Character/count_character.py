def count_character(string, char):
    count = 0
    for i in range(len(string)):
        if string[i] == char:
            count += 1
    return count
text = "banana"
ch = "a"
print(count_character(text, ch))
