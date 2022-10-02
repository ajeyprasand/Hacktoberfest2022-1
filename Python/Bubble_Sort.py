
def bubbleSort(arr):
    #swapped is used to check if the given list of elements are already sorted or not
    swapped = False
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
          #This condition is executed when the given list of elements is already sorted,so we can exit the function right away
            return
