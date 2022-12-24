"""
Link: https://leetcode.com/problems/first-unique-character-in-a-string/description/

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict_cnt = {}
        length = len(s)
        for i in range(length):
            if s[i] not in dict_cnt:
                dict_cnt[s[i]] = 0
            dict_cnt[s[i]] += 1

        for k in range(length):
            if dict_cnt[s[k]] == 1:
                return k
        return -1
