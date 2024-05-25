#Create a new array for counting how many there are of the different values.
#Go through the array that needs to be sorted.
#For each value, count it by increasing the counting array at the corresponding index.
#After counting the values, go through the counting array to create the sorted array.
#For each count in the counting array, create the correct number of elements, with values that correspond to the counting array index.
#complexity - O(n)
def counting_sort(arr):
    n = len(arr)
    print(n)

    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1
    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

#Input from the user
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

#calling the function
counting_sort(arr)

#Printing the sorted array
print("Sorted array: ",arr)
