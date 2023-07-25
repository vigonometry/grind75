from typing import List

def two_sum(nums: List[int], target: int) -> int:
    d = {}
    for i in range(len(nums)):
        m = target - nums[i]
        if m in d:
            return [d[m], i]
        d[nums[i]] = i