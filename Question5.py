# Print only even digit in number
# sum of only even digit in a number

num = "123456"

for i in num:
    d = int(i)
    if d % 2 == 0:
        print(d)