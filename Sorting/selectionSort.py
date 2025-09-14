def selectioonSort(arr):
    n = len(arr)   #length of array

    for i in range(n):  #traversing through all elements

        min = i # assuming first element of unsorted array as minimum

        for j in range(i+1,n): #traversing through unsorted elements
            if arr[j] < arr[min]: #comparing with assumed minimum
                min = j #updating index of minimum element if any element is smaller than assumed minimum

        arr[i] , arr[min] = arr[min], arr[i] #swapping minimum element with first element of unsorted array
        
    return arr

arr1 = [7,5,6,53,9]
print(selectioonSort(arr1))