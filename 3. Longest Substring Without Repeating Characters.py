"""
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_s = {}
        left = 0
        for right in range(len(s)):
            dict_s[s[right]] = dict_s.get(s[right], 0) + 1

            if max(dict_s.values()) > 1:
                dict_s[s[left]] -= 1
                left += 1
        return len(s) - left
