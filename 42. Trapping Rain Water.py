"""
Link: https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water
it can trap after raining.
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        top = height.index(max(height))

        cur_top = 0
        ans = 0
        for i in range(top):
            if height[i] > cur_top:
                cur_top = height[i]
            else:
                ans += cur_top - height[i]

        cur_top = 0
        for i in reversed(range(top, len(height))):
            if height[i] > cur_top:
                cur_top = height[i]
            else:
                ans += cur_top - height[i]
        return ans
    