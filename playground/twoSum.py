"""
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    p1 = 0
    p2 = p1 + 1
    temp = target - nums[p1] # 6 - 3 = 3
    while nums[p1] + nums[p2] != target:

        if nums[p2] == temp:
            return [p1, p2]

        elif nums[p2] != temp:
            p2 += 1

        if p2 == len(nums) - 1:
            p1 += 1
            p2 = p1 + 1

