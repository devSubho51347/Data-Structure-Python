# Find Minimum in Rotated Sorted Array - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/


class Solution:
    def findMin(self, nums: List[int]) -> int:
        ### Whenever a sorted array is rotated , one half of the array will be sorted and the other half will be unsorted. 

        # My approach will be to identify the sorted half , find the minimum value of the sorted half and find the minimum value locally

        if len(nums) == 1:
            return nums[0]


        start = 0
        end = len(nums) - 1

        min_element = nums[0]

        while start <= end:
            mid = (start + end)//2

            if nums[mid] <= nums[end]:
                min_element = min(nums[mid], min_element)
                end = mid - 1

            else:
                
                min_element = min(nums[start], min_element)
                start  = mid + 1

        return min_element        

