def rec_binary_search(arr,target, start , end):
    if start > end:
        return - 1
    
    mid = (start + end)//2
    
    if arr[mid] == target:
        return 1
    
    if arr[mid] >= target:
        end = mid - 1
    
    else:
        start = mid + 1
        
    return rec_binary_search(arr,target,start,end)


####  Method to take an input  ####

print("Enter The total no fo elements in the array:")

n = int(input())

print(f"There will be {n} elements in the input. Enter the elements of the list")

arr = [int(input()) for i in range(n)]

print("The input array is", arr)

print("target element is")

target = int(input())

if rec_binary_search(arr,target,0, len(arr) - 1) == -1:
    print("Element is not present in the array")\

else:
    print("Element is present in the array")              