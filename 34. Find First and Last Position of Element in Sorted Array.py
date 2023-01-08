"""
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target
value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        def lbinsearch(l, r):
            while l < r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m
            return -1 if nums[l] != target else l

        def rbinsearch(l, r):
            while l < r:
                m = (l + r + 1) // 2
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m
            return l

        first = lbinsearch(0, (len(nums) - 1))
        if first == -1:
            return [-1, -1]
        return [first, rbinsearch(0, len(nums) - 1)]
