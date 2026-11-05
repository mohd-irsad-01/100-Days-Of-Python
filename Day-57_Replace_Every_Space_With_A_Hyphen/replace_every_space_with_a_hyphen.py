def replace_space(string):
    
    result = ""

    for i in range(len(string)):
        if string[i] == ' ':
            result += "-"
        else:
            result += string[i]
    return result

text = input("Enter a string")
print(replace_space(text))
