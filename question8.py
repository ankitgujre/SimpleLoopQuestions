# print sum of element in list

data = [1,2,3,4,5,6,7]
total = 0
# for i in data:
#     print(i)

# for i in range(len(data)):
#     print(i, " ", data[i])

for i in data:
    total += i
print(total)

# print only even number in a list?


for i in data:
    if i % 2 == 0:
        print("even", i, end=" ")

        

# Print the sum of even/odd element in list

evensum = 0
oddsum = 0

for i in data:
    if i % 2 == 0:
        evensum += i
    else:
        oddsum += i

print("Sum of even numbers:", evensum)
print("Sum of odd numbers:", oddsum)