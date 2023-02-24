from typing import List


# Link: https://leetcode.com/problems/two-sum/
class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [index, hashmap[complement]]
            hashmap[num] = index
