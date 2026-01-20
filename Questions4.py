# count the digit of number without using len() function

# num = "123"
# count = 0

# for i in num:
    
#     count += 1

# print(count)

# sum of digit in a number without using sum

# n = "1234"
# ts = 0

# for i in n:
#     ts += int(i)
#     print(ts)
    
# print(ts)

# Print only even digit in number

num = "123456"

for i in num:
    d = int(i)
    if d%2 == 0:
        print("even = ", d)
        
# sum of only even digit in a number

n = "123"
es = 0

for i in n:
    d = int(i)
    if d%2 == 0:
        print(d)
        es += d
print("sum of even = ", es)