from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        while s <= e:
            m = s + (e - s)//2
            if nums[m] == target:
                return m
            if nums[m] < target:
                s = m + 1
            else:
                e = m - 1
        return -1