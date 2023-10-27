# Insertion sort is a sorting algorithm that works by inserting each element of an unsorted list into the sorted part of the list in its correct position. The algorithm starts at the beginning of the list and iterates over each element. For each element, the algorithm finds the correct position in the sorted part of the list and inserts the element there.

def insertionsort(arr):

    for i in range(1 , len(arr)):

        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]: # if the previous element was smaller 
            arr[j+1] = arr[j]
            j-= 1

        arr[j+1] = key # insert the key in the place
    return arr

arr = [4 , 2  , 5 , 2 , 3 , 1]
print(arr)
print(insertionsort(arr))
