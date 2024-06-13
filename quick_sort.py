#Choose a value in the array to be the pivot element.
#Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
#Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
#Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.
#complexity - O(nlogn)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

