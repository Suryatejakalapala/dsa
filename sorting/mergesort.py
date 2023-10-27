# Merge sort is a divide-and-conquer sorting algorithm. It works by dividing the unsorted list into two halves, sorting each half recursively, and then merging the sorted halves back together. The algorithm continues dividing and merging the list until the entire list is sorted.

def merge(left , right):
    merged_array = []
    i , j = 0 , 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i+=1
        else:
            merged_array.append(right[j])
            j+=1

    merged_array += left[i:]
    merged_array += right[j:]

    return merged_array

def mergesort(arr):

    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = mergesort(arr[mid:])
    right = mergesort(arr[:mid])

    return merge(left , right)

arr = [3, 4, 1 , 5 ,2 , 4 , 2]
print(arr)
print(mergesort(arr))



