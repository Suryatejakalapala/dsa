# Selection sort is another simple sorting algorithm. It works by finding the smallest element in the unsorted list and swapping it with the first element. The algorithm then repeats this process with the remaining elements in the list.


def selectionsort(arr):
    
    for i in range(len(arr) - 1):
        # starting position lets assume as min 
        min_index = i
        
        for j in range(i+1 , len(arr)):
            if arr[j] < arr[min_index]: # if we found another min then change the index
                min_index = j

        arr[i] , arr[min_index] = arr[min_index] , arr[i] # swap with the min 
    return arr

arr = [2 , 4 , 2 , 6 , 1 , 3]
print(arr)
print(selectionsort(arr))
