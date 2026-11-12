num = int(input("Enter a number: "))

ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "Fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "", "twenty", "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"]

words = ""

if num == 0:
    words = "zero"
if num >= 1000:
    words += ones[num // 1000] + " thousand "
    num = num % 1000
if num >= 100:
    words += ones[num // 100] + " hundred "
    num = num % 100
if num >= 10 and num <= 19:
    words += teens[num - 10]
    num = 0
elif num >= 20:
    words += tens[num // 10] + " "
    num = num % 10
if num > 0:
    words += ones[num]
print(words.strip())
