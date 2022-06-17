# find the if sum of two elements is a value
# find pythagoream triplets
def sum_of_two(arr, val):
    found = set()
    for el in arr:
        if val - el in found:
            return True
        found.add(el)
    return False
def func(arr):
    n = len(arr)
    for i in range(n):
        if sum_of_two(arr[:i]+arr[i+1:], arr[i]):
            return True
    return False


