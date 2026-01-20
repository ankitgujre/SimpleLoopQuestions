# Print maximum digit in a number


num = "123456"

maxdigit = 0

for i in num:
    d = int(i)
    if d > maxdigit:
        maxdigit = d

print("Maximum digit =", maxdigit)