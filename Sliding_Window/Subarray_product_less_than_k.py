# def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:

#         start = 0
#         end = 0
#         count = 0
#         product = 1

#         if k == 0:
#             return 0 

#         if k == 1:
#             return 0
        
#         while end < len(nums):
#             product = product*nums[end]
            
#             while product >= k:
#                 product = product/nums[start]
#                 start = start + 1
            
#             count = count + end - start + 1
#             end = end + 1
#         return count
            
    
# print(numSubarrayProductLessThanK([10,5,2,6], k = 100))    


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count = 0
        current = 0
        best = 0
        for fruit in fruits:
            if fruit == last_fruit or fruit == second_last_fruit:
                current += 1
            else:
                current = last_fruit_count + 1
            if fruit == last_fruit:
                last_fruit_count += 1
            else:
                second_last_fruit = last_fruit
                last_fruit = fruit
                last_fruit_count = 1
            best = max(best, current)
        return best    