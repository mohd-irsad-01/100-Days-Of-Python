# Q. Find Non-Repeating Character


text = input("Enter String: ")

for char in text:
    if text.count(char) == 1:
        print(char, end=" ")
