# https://leetcode.com/problems/sqrtx/
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        # 1. 确定答案范围
        start, end = 1, x
        # 2. 套二分模版
        while start + 1 < end:
            mid = (start + end) // 2
            # 3. 核心：验证答案偏大还是偏小
            # <=x 需要往大调，把start移到mid
            if mid * mid <= x:
                start = mid
            else:
                end = mid

        if end * end <= x:
            return end
        if start * start <= x:
            return start
        return -1
