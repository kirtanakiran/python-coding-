#Choose a value in the array to be the pivot element.
#Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
#Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
#Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.
#complexity - O(nlogn)
def insertion_sort(arr):
    n = len(arr)
    print(n)

    for i in range(1, n):
        index = i
        curr_val = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > curr_val:
                arr[j+1] = arr[j]
                index = j
            else:
                break
        arr[index] = curr_val

#Input from the user
arr = list(map(int, input("Eter the elements of the array :").split()))

#calling the function
insertion_sort(arr)

#Print the sorted array
print("Sorted array :",arr)

