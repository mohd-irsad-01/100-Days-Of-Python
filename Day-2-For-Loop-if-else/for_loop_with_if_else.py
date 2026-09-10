# Day-02 - For loop with if-else
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
odd_sum = 0
for i in l:
    if i % 2 == 0:
        print(f"{i} is Even")
        even_sum += i
    else:
        print(f"{i} is Odd")
        odd_sum += i
print(f"Even sum = {even_sum}, Odd sum = {odd_sum}")        
