# Q. Check if two strings are Anagram.
# Example: listen & silent = Anagram

s1 = input('Enter first: ').lower()
s2 = input('Enter second: ').lower()

if sorted(s1) == sorted(s2):
    print('Anagram')
else:
    print('Not Anagram')

# Logic: sorted() compare
# listen --> eilnst, silent --> eilnst
