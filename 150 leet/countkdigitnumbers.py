def CountKDigitNumbers(arr, n, k):
    count = 0
    for num in arr:
        if len(str(num)) == k:
            count += 1
    return count

