# Problem Statement - Leetcode - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


### Solution with 2 binary search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start  = 0 
        end = len(nums) - 1

        low_index = 0
        high_index = 0

        if len(nums) == 0:
            return [-1,-1]


        def find_min_index(nums,target,start,end,lower_index):
            lower_index = lower_index
            if start > end:
                return lower_index
            while start <= end:
                mid = (start+end)//2
                if nums[mid] == target:
                    lower_index = mid
                    end = mid - 1
                if nums[mid] < target:
                    start = mid + 1  
            return lower_index  

        def find_max_index(nums,target,start,end,higher_index):
            higher_index = higher_index
            if start > end:
                return higher_index
            while start <= end:
                mid = (start+end)//2
                if nums[mid] == target:
                    higher_index = mid
                    start = mid + 1

                if nums[mid] > target:
                    end = mid - 1  
            return higher_index 
              



        while start <= end:
            mid = (start + end)//2

            if nums[mid] == target:
                lower_index = find_min_index(nums,target,start,mid,mid)
                higher_index = find_max_index(nums,target,mid,end,mid)
                return [lower_index,higher_index]

            if nums[mid] < target:
                start  = mid + 1
            elif nums[mid] > target:
                end = mid - 1 
        print("start element is",start,end)
        if start > end:
            return [-1,-1]               

        