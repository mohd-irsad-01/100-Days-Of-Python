# Q. Remove characters from first string present in second.

str1 = input('Enter first string: ')
str2 = input('Enter second string: ')

result = ''
for char in str1:
    if char not in str2:
        result += char
print('Result: ', result)

# Ex: hello, lo -> he 
