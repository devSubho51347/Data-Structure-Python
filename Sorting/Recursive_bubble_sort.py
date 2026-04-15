## Solved it on my own in first attempt

def recursive_bubble_sort(arr, k):
    if len(arr) == k:
        return arr
    
    def sort_element(arr,k):
        for i in range(len(arr) - k):
            if arr[i] > arr[i + 1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]
        
        print("First bubble_sorted_array:", arr)
        return arr    
    
    sorted_array = sort_element(arr,k)
    k = k + 1
    
    return recursive_bubble_sort(sorted_array,k)

print("Enter the unsorted list:") 

li =  [int(input()) for ele in range(5)]
                
print("List has been sorted")
print(recursive_bubble_sort(li,1))     
            
            