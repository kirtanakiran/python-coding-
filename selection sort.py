#How it works?
#Go through the array to find the lowest value.
#Move the lowest value to the front of the unsorted part of the array.
#Go through the array again as many times as there are values in the array.
#time complexity - O(n^2)
def selection_sort(arr):
    n = len(arr)
    print(n)

    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i] , arr[min_index] = arr[min_index] , arr[i]

#input from the user 
arr = list(map(int, input("Enter the elements of the array ").split()))

#calling the function
selection_sort(arr)

#printing the sorted array
print("Sorted array is:",arr)

