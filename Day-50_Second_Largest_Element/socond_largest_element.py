def second_largest(arr):
    largest = arr[0]
    second = None

    for i in arr:
        if i > largest:
            second = largest
            largest = i
        elif i < largest:
            if second is None or i > second:
                second = i 
    return second
arr1 = [10, 12, 13, 14, 12, 14, 13, 15, 16, 17, 18, 19, 19]
arr2 = [8, 8, 8]
arr3 = [-2, -3, 0, 1]

print("arr1: ", second_largest(arr1))
print("arr2: ", second_largest(arr2))
print("arr3: ", second_largest(arr3))
