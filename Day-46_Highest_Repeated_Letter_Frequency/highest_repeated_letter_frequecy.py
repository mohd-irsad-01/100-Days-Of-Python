s = input("Enter a sentence: ")

words = s.split()
best_word = ""
highest_frequency = 0
for word in words:
    frequency = 0
    for ch in word:
        count = 0
        for other in word:
            if ch == other:
                count += 1
        if count > frequency:
            frequency = count
    if frequency > highest_frequency:
        highest_frequency = frequency
        best_word = word
        
print("Word: ", best_word)
print("Repeated-Letter Frequency: ", highest_frequency)
