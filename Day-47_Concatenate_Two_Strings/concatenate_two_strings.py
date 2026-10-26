s = input("Enter more than one strings: ")

str1 = ""
str2 = ""
separater_found = False

for ch in s:
    if ch == "," or ch == " ":
        separater_found = True
    elif not separater_found:
        str1 += ch
    else: 
        str2 += ch

print(str1 + str2)
