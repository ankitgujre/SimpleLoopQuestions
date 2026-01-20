# Armstrong

n = input("Enter a Number: ")
power = len(n)
ans = 0

for i in n:
    ans += int(i)**power
    
if ans == int(n):
    print("Armstrong")
else:
    print("Not an Armstrong")