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
