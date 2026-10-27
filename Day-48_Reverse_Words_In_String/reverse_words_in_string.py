text = input("Enter a string: ")

words = text.split()
reversed_word = words[::-1]
result = " ".join(reversed_word)

print(result)
