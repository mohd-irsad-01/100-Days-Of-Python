# 1. Count Frequency
def count_frequency(words):
    freq = {}
    for w in words:
        if w in freq:
            freq[w] += 1 
        else:
            freq[w] = 1
    return freq


# 2. Merge Dicts
def merge_dicts(d1, d2):
    merged = {}
    for k in d1:
        merged[k] = d1[k]
    for k in d2:
        merged[k] = d2[k]
    return merged


# 3. Max value key
def max_value_key(d):
    max_key = None
    max_value = 0
    for k in d:
        if d[k] > max_value:
            max_value = d[k]
            max_key = k
    return max_key



# Calls
print(count_frequency(["a", "b", "a"]))
print(merge_dicts({"a": 1}, {"b": 2}))
print(max_value_key({"a": 10, "b": 30}))
