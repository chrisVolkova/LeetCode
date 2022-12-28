"""
Link: https://leetcode.com/problems/is-subsequence/description/

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of
the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        idx_1, idx_2 = 0, 0
        cnt = 0
        while idx_2 < len(t) and idx_1 < len(s):
            if s[idx_1] == t[idx_2]:
                idx_1 += 1
                cnt += 1
            idx_2 += 1

        return cnt == len(s)
