def Binary_search(arr, target):
    ### Non recursive approach #####
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end)//2
        print("Mid element", mid, " value will be", arr[mid])
        if arr[mid] == target:
            return 1
        
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    
    return -1         
                


####  Method to take an input  ####

print("Enter The total no fo elements in the array:")

n = int(input())

print(f"There will be {n} elements in the input. Enter the elements of the list")

arr = [int(input()) for i in range(n)]

print("The input array is", arr)

print("target element is")

target = int(input())

if Binary_search(arr,target) == -1:
    print("Element is not present in the array")\

else:
    print("Element is present in the array")        
    
#### Completed ###    