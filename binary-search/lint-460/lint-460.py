# https://www.lintcode.com/problem/find-k-closest-elements/?_from=ladder&&fromId=1
class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """

    def kClosestNumbers(self, A, target, k):
        """
        1. 找到分界线，确定left和right两个指针，也就是最接近target的两个数，他们肯定是相邻的
        right是>=target的第一个数的位置
        """
        right = self.findUpperClosest(A, target)
        left = right - 1

        """
        2. 在一个k的循环中，两指针从中间往两边拓展，依次比较left和right谁更接近target
        """
        results = []
        for _ in range(k):
            if self.ifLeftCloser(A, target, left, right):
                results.append(A[left])
                left -= 1
            else:
                results.append(A[right])
                right += 1

        return results

    def findUpperClosest(self, A, target):
        start, end = 0, len(A) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if A[mid] >= target:
                end = mid
            else:
                start = mid

        # 注意这里是找>=target的第一个位置
        if A[start] >= target:
            return start

        if A[end] >= target:
            return end

        # 找不到的情况，整个数组都小于target,那么结果按距离排是[A[-1],A[-2],...A[0],left指针从len(A)-1开始
        return len(A)

    def ifLeftCloser(self, A, target, left, right):
        if left < 0:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target
