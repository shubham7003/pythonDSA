def insertionSort(arr):
    for i in range(1,len(arr)):   #Traversing through 1 to len(arr)-1
        key = arr[i];  # Element to be compared at each iteration
        j = i-1  # Index of element that be compared with key at each iteration
        while j>=0 and key < arr[j]:   #shifiting elements that are greater than key to one position ahead of their current position
            arr[j+1] = arr[j]  #shifting element to one position ahead
            j -= 1  # decrementing j for ending while loop and comparing with next
        arr[j+1] = key #key placing key after the element just smaller than it.  

    
    return arr

a = [12,11,13,5,6]
print(insertionSort(a))