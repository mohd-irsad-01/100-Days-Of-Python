# Q. Capitalize first and last character of each word

text = input('Enter string: ')

result = ''
words = text.split()
for word in words:
    if len(word) == 1:
        result += word.upper() + ' '
    else:
        new_word = word[0].upper() + \
                   word[1:-1] + \
                   word[-1].upper()
        result += new_word + ' '

print(f'Result: {result.strip()}')

# Ex: hello world -> HellO WorlD
