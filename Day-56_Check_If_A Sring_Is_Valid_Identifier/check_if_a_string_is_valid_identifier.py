def check_identifier(string):
    if len(string) == 0:
        return "Invalid"
    if not (string[0].isalpha() or string[0] == '_'):
        return "Invalid"
    for i in range(len(string)):
        if not (string[i].isalnum() or string[i] == '_'):
            return "Invalid"
    return "Valid"

text = input("Enter a string")
print(check_identifier(text))
