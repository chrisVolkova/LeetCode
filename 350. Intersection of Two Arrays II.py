"""
Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear
as many times as it shows in both arrays and you may return the result in any order.
"""


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        cnt_set = set(nums1).intersection(set(nums2))
        if len(cnt_set) == 0:
            return []
        dict1 = {}
        for num in nums1:
            if num not in dict1:
                dict1[num] = 0
            dict1[num] += 1
        dict2 = {}
        for num in nums2:
            if num not in dict2:
                dict2[num] = 0
            dict2[num] += 1

        def append(num, k, list):
            for i in range(k):
                list.append(num)

        ans = []
        for num in cnt_set:
            if dict1[num] <= dict2[num]:
                append(num, dict1[num], ans)
            else:
                append(num, dict2[num], ans)
        return ans


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        first = second = 0
        ans = []
        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[second]:
                first += 1
            elif nums1[first] > nums2[second]:
                second += 1
            else:
                ans.append(nums1[first])
                first += 1
                second +=1
        return ans
