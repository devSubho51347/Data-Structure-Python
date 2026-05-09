# Leetcode problem - https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        if target == nums[-1]:
            return len(nums) - 1
        if target > nums[-1]:
            return len(nums)

        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end)//2

            if start == end:
                # if nums[start] == target:
                #     return start
                if nums[start] < target:
                    return start + 1
                else:
                    return start

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            if nums[mid] > target:
                end = mid - 1
        return start        