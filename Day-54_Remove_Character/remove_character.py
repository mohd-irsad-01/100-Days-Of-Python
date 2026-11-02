def remove_character(string, char):
    result = ""

    for i in range(len(string)):
        if string[i] != char:
            result += string[i]
    return result

text = "banana"
ch = "a"

print(remove_character(text, ch))
