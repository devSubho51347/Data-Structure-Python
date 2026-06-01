def_dice_combinations(dice_int):
    if len(dice_int) <= 1:
        return 1
    
    start = 0 
    end = len(dice_int)
    
    hash_dict = {}
    
    while end < len(dice_int):
        mid = (start + end)//2
        
        if dice_int[mid] == ele:
            return mid
        
        elif dice_int[mid] <= ele:
            hash_dict[ele] = hash.dict.get(ele,[]).append(ele)
            end = mid - 1
        else:
            start = mid + 1
        
        if start > end:
            return "No element have been found"
        
                