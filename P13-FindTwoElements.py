# find the if sum of two elements is a value
# find pythagoream triplets
def find_sum_of_two(arr, val):
    found_values = set()
    for el in arr:
        if val - el in found_values:
            return True
        found_values.add(el)
    return False 

def find_pythagorean_triplet(arr):
    arr = [arr[i]**2 for i in len(arr)]
    for i, el in enumerate(arr):
        find_sum_of_two(arr[:i]+arr[i+1:], el)

