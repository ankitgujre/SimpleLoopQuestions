# Print Even number from 1 to 10

numbers = [1,2,3,4,5,6,7,8,9,10]

for num in numbers:
    if num % 2 == 0:
        print(num)
        
        
print("Odd")

for num in numbers:
    if num % 2 != 0:
        print(num)
        
        
print("While")

i = 0
while i < len(numbers):
    num = numbers[i]
    if num % 2 == 0:
        print(num)
    i += 1
    
print("While Odd")

i = 0
while i < len(numbers):
    num = numbers[i]
    if num % 2 != 0:
        print(num)
    i += 1