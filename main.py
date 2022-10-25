# Part (1)
numbers = [ [99,11,66,86,55],[44,21,65,88,24],[33,77,32,33,34]]

# Part (2)
print("Sum of rows: ",end=" ")
for i in numbers:
    print(sum(i),end=" ")
print(end="\n")

print("Sum of columns: ",end=" ")
for i in zip(*numbers):
    print(sum(i),end=" ")
print(end="\n")
# Part (3)
sum_list = []
for i in numbers:
    sum_list.append(sum(i))

greatest = sum_list.index(max(sum_list))
print("The row that has greatest sum: ",greatest)

# Part (4)
max_list = []
for i in numbers:
    max_list.append(max(i))

print("The greatest number: ",max(max_list))
