def Insertion_sort(arr):
    if len(arr) < 2:
        return arr
    
    
    def sort_array(arr):
        
        j = len(arr) - 1
        
        while j > 0:
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j-1],arr[j]
            else:
                break
            j = j - 1
        return arr        
    
    i = 1
    while i < len(arr):
        sorted = sort_array(arr[:i+1])
        arr[:i+1] = sorted
        print("array is:", arr)
        i = i + 1
        
    return arr   



#### User Input ######3
print("Enter the unsorted list:") 

li =  [int(input()) for ele in range(5)]
                
print("List has been sorted")
print(Insertion_sort(li))   



#### More modular code u can find here - 

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]          # element to insert
        j = i - 1

        # shift elements greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # place key at correct position
        arr[j + 1] = key

    return arr


# Example usage
arr = [8, 3, 5, 2, 9, 1, 4]
print(insertion_sort(arr))
        
        
        