#### Function for recursive insertion sort

## Bottom up approach

def recursive_insertion_sort(arr,end):
    if end  == len(arr):
        return arr
    
    def insert_element(arr,end):
        key = arr[end]
        
        j = end - 1
        
        while (j >= 0) and (arr[j] > key):
            arr[j+1] = arr[j]
            j = j - 1
        
        arr[j + 1] = key
        
        print("End is", end, arr, key)
        
        return arr
    
    sorted_sub_array = insert_element(arr,end)
    end = end + 1
    
    return recursive_insertion_sort(sorted_sub_array,end) 



## top down approach 

def insertion_sort_recursive(arr, n=None):
    # initialize n
    if n is None:
        n = len(arr)
    
    # base case
    if n <= 1:
        return
    
    # sort first n-1 elements
    insertion_sort_recursive(arr, n - 1)
    
    # insert last element at correct position
    key = arr[n - 1]
    j = n - 2
    
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    
    arr[j + 1] = key   
        



### Here goes your input

print("Enter the no of elements in your list")

n = int(input())

li = [int(input()) for i in range(n)]

print("Unsorted array", li)

print(recursive_insertion_sort(li,1))
