"""
Link: https://leetcode.com/problems/maximize-distance-to-closest-person/description/

You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to the closest person.
"""


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        length = len(seats)
        left = length * [0]
        cnt = 0
        cur_point = 0
        for i in range(length):
            if seats[i] == 1:
                cnt += 1
                cur_point = 0
            else:
                if cnt == 0:
                    cur_point = float('inf')
                else:
                    cur_point += 1
            left[i] = cur_point

        cnt = 0
        for i in reversed(range(length)):
            if seats[i] == 1:
                cnt += 1
                cur_point = 0
            else:
                if cnt == 0:
                    cur_point = float('inf')
                else:
                    cur_point += 1
            left[i] = min(cur_point, left[i])

        return max(left)
    