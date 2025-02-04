# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap={} #too: index
        for i, n in enumerate(nums):
            zoruu=target-n
            if zoruu in hashmap:
                return [hashmap[zoruu],i]
            hashmap[n]=i
        return 
        


nums=[1,2,3,4,5,6,7,8,9]
target=17 #8+9
print(twoSum(nums,target)) #output=[7,8]

    


