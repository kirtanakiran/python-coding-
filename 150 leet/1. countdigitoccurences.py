def CountDigitOccurrences(l, u, x):
    count = 0
    target_digit = str(x)  # Convert the integer x to its string representation

    for i in range(l, u + 1):
        number_str = str(i)  # Convert the number to string
        count += number_str.count(target_digit)  # Count occurrences of target_digit in the number_str

    return count

