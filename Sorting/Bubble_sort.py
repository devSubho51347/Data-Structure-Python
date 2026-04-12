### code for bubbler sort

def bubble_sort(arr):
    
    if len(arr) < 2:
        return arr
    
    start = 0
    i = 0
    
    while i < len(arr) - 1:
        start = i
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        i = i + 1        
    return arr            
 
print("Enter the unsorted list:") 

li =  [int(input()) for ele in range(5)]
                
print("List has been sorted")
print(bubble_sort(li))                