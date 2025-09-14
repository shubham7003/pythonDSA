def bubbleSort(arr):
    n = len(arr)  #length of array
    
    for i in range(n-1): #Number of passes through the array
        swaped = False # checking any swap is done or not

        for j in range(n-1-i): # loop through unsorted element
            if arr[j] > arr[j+1]: #comparing adjacent elements
                arr[j], arr[j+1] = arr[j+1], arr[j]  #swapping if elements are in wrong order
                swaped = True #setting swaped to true if swap is done

        if not swaped:
            break

    return arr


