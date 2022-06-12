arr = [12, 11, 13, 5, 6]

def InsertionSort(arr):
    #O(n^2)
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
 
 
# Driver code to test above
InsertionSort(arr)
print ("InsertionSort result is:")
for i in range(len(arr)):
    print ('{}'.format(arr[i]))

def SelectinSort(arr):
    #O(n^2)
    for i in range(len(arr)):
      
        # Find the minimum element in remaining 
        # unsorted array
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
                
        # Swap the found minimum element with 
        # the first element        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

SelectinSort(arr)
print ("SelectinSort result is:")
for i in range(len(arr)):
    print ('{}'.format(arr[i]))

def bubbleSort(arr):
    #O(n^2)
    n = len(arr)
 
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubbleSort(arr)
print ("bubbleSort result is:")
for i in range(len(arr)):
    print ('{}'.format(arr[i]))


def Merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def MergeSort(arr, l, r):
    #O(N*LOG(N))
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        MergeSort(arr, l, m)
        MergeSort(arr, m+1, r)
        Merge(arr, l, m, r)

MergeSort(arr, 0, len(arr)-1)
print ("MergeSort result is:")
for i in range(len(arr)):
    print ('{}'.format(arr[i]))

def Partition(l, r, arr):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = arr[r], l
    for i in range(l, r):
        if arr[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    arr[ptr], arr[r] = arr[r], arr[ptr]
    return ptr
 
# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.
 
 
def QuickSort(l, r, arr):
    #O(N*LOG(N))
    if len(arr) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return arr
    if l < r:
        pi = Partition(l, r, arr)
        QuickSort(l, pi-1, arr)  # Recursively sorting the left values
        QuickSort(pi+1, r, arr)  # Recursively sorting the right values
    return arr

QuickSort(0, len(arr)-1, arr)
print ("QuickSort result is:")
for i in range(len(arr)):
    print ('{}'.format(arr[i]))