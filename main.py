def binary_search(sequence, target):
    low = 0
    high = len(sequence)-1

    while low <= high:
        mid = (low + high)//2
        middle_number = sequence[mid]

        if middle_number == target:
            return f"the target is at position: {mid}"
        elif target > middle_number:
            low = mid + 1
        else:
            high = mid - 1 

    return f"your target is not in the sequence"
print(binary_search(sequence=[1,2,3,4,5,6,7,8,9],target=11))

