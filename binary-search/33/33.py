# https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
Solution 1
用两次二分的方法。

第一次二分：找到最小数的位置，参考 find minimum number in rotated sorted array
第二次二分：确定 target 在左侧区间还是右侧，用一个普通的二分法即可找到。
"""


class Solution:
    def search(self, A, target):
        if not A:
            return -1

        index = self.find_min_index(A)
        if A[index] <= target <= A[-1]:
            return self.binary_search(A, index, len(A) - 1, target)
        return self.binary_search(A, 0, index - 1, target)

    def find_min_index(self, A):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < A[end]:
                end = mid
            else:
                start = mid
        if A[start] < A[end]:
            return start
        return end

    def binary_search(self, A, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1


"""
Solution 2: 一次二分
"""


class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """

    def search(self, A, target):
        if not A:
            return -1

        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # 在左上角的判断条件
            if A[mid] >= A[start]:
                if A[start] <= target <= A[mid]:
                    # 在左侧
                    end = mid
                else:
                    start = mid
            else:
                if A[mid] <= target <= A[end]:
                    start = mid
                else:
                    end = mid

        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
