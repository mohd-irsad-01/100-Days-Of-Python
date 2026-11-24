import copy

# Original list
original = [[10, 20], [30, 40]]
print("Original List:", original)

# Normal copy
normal_copy = original
normal_copy[0][0] = 100
print("\nNormal copy:")
print("Original:", original)
print("Copy:", normal_copy)

# Reset original list
original = [[10, 20], [30, 40]]

# Shallow copy
shallow_copy = copy.copy(original)
shallow_copy[0][0] = 200
print("\nShallow copy:")
print("Original:", original)
print("Copy:", shallow_copy)

# Reset original list
original = [[10, 20], [30, 40]]

# Deep copy
deep_copy = copy.deepcopy(original)
deep_copy[0][0] = 300
print("\nDeep copy:")
print("Original:", original)
print("Copy:", deep_copy)
