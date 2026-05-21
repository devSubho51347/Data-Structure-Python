def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:

        start = 0
        end = 0
        count = 0
        product = 1

        if k == 0:
            return 0 

        if k == 1:
            return 0
        
        while end < len(nums):
            product = product*nums[end]
            
            while product >= k:
                product = product/nums[start]
                start = start + 1
            
            count = count + end - start + 1
            end = end + 1
        return count
            
    
print(numSubarrayProductLessThanK([10,5,2,6], k = 100))    