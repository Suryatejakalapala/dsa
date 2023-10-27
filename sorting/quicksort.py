# Quicksort is a divide-and-conquer sorting algorithm. It works by partitioning the unsorted list around a pivot element and then sorting the two sublists recursively. The algorithm continues partitioning and sorting the sublists until the entire list is sorted.

def quicksort(arr):
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]

        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
    

arr = [3, 4, 1 , 5 ,2 , 4 , 2]
print(arr)
print(quicksort(arr))