#taking array as a input
list = []
n = int(input("Enter the number of elements: "))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
print(list)

#Intialising the variable to the first element of the array
minval = list[0]

#traversing throught the array 
for i in list:
    if i<minval:
        minval = i
print("Lowest value: ",minval)
