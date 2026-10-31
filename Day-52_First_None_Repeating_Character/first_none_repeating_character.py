def first_none_repeating(string):
    for i in range(len(string)):
        count = 0
        for j in range(len(string)):
            if string[i] == string[j]:
                count += 1
        if count == 1:
            return string[i]
    return None

text = "programming"
print(first_none_repeating(text))
