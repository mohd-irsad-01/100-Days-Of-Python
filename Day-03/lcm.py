# WAP to calculate the LCM of a given numbers.
num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
if num1 < num2:
    small = num1
else:
    small = num2
for i in range(1,small+1):
    if num1%i == 0 and num2%i == 0:
        HCF = i
LCM = (num1*num2)//HCF       
print("LCM of a given number is ", LCM) 