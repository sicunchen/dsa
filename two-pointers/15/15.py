# https://leetcode.com/problems/3sum/

"""
Time: O(nlogn+n^2)->O(n^2), twoSum is O(n) and we call it n times
Space: O(logn) to O(n), depending on the implementation of the sorting algorithm. For the purpose of complexity analysis, we ignore the memory required for the output.
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        length = len(nums)
        for i in range(0, length - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, length - 1, -nums[i], results)
        return results

    def find_two_sum(self, nums, left, right, target, results):
        last_triplet = [None, None, None]
        while left < right:
            if nums[left] + nums[right] == target:
                if ([-target, nums[left], nums[right]]) != last_triplet:
                    results.append([-target, nums[left], nums[right]])
                last_triplet = [-target, nums[left], nums[right]]
                left, right = left + 1, right - 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1

