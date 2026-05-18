# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=problem-list-v2&envId=sliding-window

'''
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
'''


#### Solution using hashmap without sliding window 

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        my_dict = {}

        for i in range(len(nums)):
            my_dict[nums[i]] = my_dict.get(nums[i],[])+ [i]

        for ele in my_dict.keys():
            if len(my_dict[ele]) > 1:
                i = 1
                while i < len(my_dict[ele]):
                    if (my_dict[ele][i] - my_dict[ele][i-1]) <= k:
                        return True
                    i = i + 1
            else:
                pass
        return False        
    
#### For solution using sliding window - Use a combination of hashset and sliding window

    
