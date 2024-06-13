#Choose a value in the array to be the pivot element.
#Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
#Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
#Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.
#complexity - O(nlogn)
def quick_sort_in_place(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

