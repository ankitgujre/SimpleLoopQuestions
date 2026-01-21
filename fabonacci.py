n = int(input("Enter number: "))

a , b = 0, 1

for i in range( n):
    c = a+b
    print(c)
    a = b
    b = c
# print(c, end=" ")

nm = int(input("Enter num: "))

fs, sec = 0, 1

for i in range(nm):
    print(fs, end=" ")
    fs, sec = sec, fs+sec