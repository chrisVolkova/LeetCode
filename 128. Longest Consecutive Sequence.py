"""
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        set_cnt = set(nums)
        for num in set_cnt:
            if num - 1 not in set_cnt:
                cnt_res = 0
                cur_num = num
                while cur_num in set_cnt:
                    cnt_res += 1
                    cur_num += 1
                res = max(cnt_res, res)
        return res
