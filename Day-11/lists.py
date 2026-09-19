# Find Largest Number in a List
def find_largest(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest


# Sum of All Numbers in a List
def sum_list(nums):
    total = 0
    for n in nums:
        total += n
    return total


# Remove Duplicates in a List
def remove_duplicates(nums):
    unique = []
    for  n in nums:
        if n not in unique:
            unique.append(n)
    return unique


# Function calls
print(find_largest([4, 7, 1, 9, 3]))
print(sum_list([1, 2, 3, 4, 5])) 
print(remove_duplicates([1, 2, 2, 3, 1]))
