"""
Link: https://leetcode.com/problems/missing-number/description/

Given an array nums containing n distinct numbers in the range [0, n], return the only
number in the range that is missing from the array.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        i = 0
        while i + 1 < len(sort_nums):
            if sort_nums[i] + 1 != sort_nums[i + 1]:
                return sort_nums[i] + 1
            i += 1
        if sort_nums[0] > 0:
            return sort_nums[0] - 1
        return sort_nums[i] + 1


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = set(nums)
        for i in range(0, len(nums)):
            if i not in n:
                return i
        return len(nums)
    