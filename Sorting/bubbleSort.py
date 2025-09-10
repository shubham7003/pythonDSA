def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        swaped = False

        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaped = True

        if not swaped:
            break

    return arr


