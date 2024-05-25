#Take the first value from the unsorted part of the array.
#Move the value into the correct place in the sorted part of the array.
#Go through the unsorted part of the array again as many times as there are values.
#complexity - O(n^2)

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

