# Q. Find the largest word in the string.

s = input("Enter a string: ")

words = s.split()
largest = ""

for word in words:
    if len(word) > len(largest):
        largest = word
print("Largest word: ", largest)
