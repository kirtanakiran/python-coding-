#Go through the array, one value at a time.
#For each value, compare the value with the next value.
#If the value is higher than the next one, swap the values so that the highest value comes last.
#Go through the array as many times as there are values in the array.
#time complexity - O(n^2)

def bubble_sort(arr):
    n = len(arr)
    print(n)
#Traverse through the array
    for i in range(n):
        swapped = False
        for j in  range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
                swapped = True

#Input from the user
arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

#calling the function
bubble_sort(arr)

#Printing the sorted array
print("Sorted array: ",arr)
