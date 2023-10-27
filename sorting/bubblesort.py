# Bubble sort is a simple sorting algorithm that works by repeatedly comparing adjacent elements in a list and swapping them if they are in the wrong order. The algorithm continues iterating over the list until no more swaps are needed.

def bubble_sort(array):
    
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1] , array[j]

array = [4 , 1 , 4 , 2 , 6 , 2]
print(array)
bubble_sort(array)
print(array)