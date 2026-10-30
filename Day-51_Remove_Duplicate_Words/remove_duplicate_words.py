def remove_duplicate_words(string):
    words = string.split()
    result = []

    for word in words:
        if word not in result:
            result.append(word)

    return " ".join(result)

text = "python is easy and python is powerful"
print(remove_duplicate_words(text))
