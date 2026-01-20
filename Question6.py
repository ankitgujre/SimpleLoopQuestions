num = "123"
even_sum = 0

for i in num:
    digit = int(i)
    if digit % 2 == 0:
        print(digit)
        even_sum += digit

print("Sum of even digits:", even_sum)