### This is a divide and conquer algorithm. it basically states that divide 2 array get them sorted and then finally merge them together

def merge_sort(arr):
    
    def merge(left,right):
        temp_array = []
        left_start = 0
        right_start = 0
        
        print("In merge sort", left , right)
        
        
        while len(temp_array) != len(left) + len(right):
            
            print("Temp_array", temp_array)
            
            if (left_start < len(left)) and (right_start < len(right)):
                
                if (left[left_start] <= right[right_start]):
                    temp_array.append(left[left_start])
                    left_start +=1
                
                else:
                    temp_array.append(right[right_start])
                    right_start +=1
        
            
                
            elif left_start < len(left):
                temp_array.extend(left[left_start:])
                
            elif right_start < len(right):
                temp_array.extend(right[right_start:]) 
                
            # if len(temp_array) == len(left) + len(right):
                # return temp_array     
        return temp_array
              
                 
    
    # Base Condition
    if len(arr) == 1:
        return arr
    
    mid = len(arr)//2
    
    print("Mid elemet is", arr[mid])
    
    left = merge_sort(arr[:mid])
    
    print("Left array is :", left)
    right = merge_sort(arr[mid:])
    
    print("Right array is", right)
    
    return merge(left,right)


#### User Input ######3
print("Enter the unsorted list:") 

# li =  [int(input()) for ele in range(5)]
li = [20,1,4,7,33,98,7]
                
print("List has been sorted")
print(merge_sort(li))   