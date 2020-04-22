class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        kth = 1
        # 用倍增法在O(log(k))时间内找到右边界
        while reader.get(kth - 1) < target:
            kth = kth * 2

        # start 也可以是 kth // 2，但是我习惯比较保守的写法
        # 因为写为 0 也不会影响时间复杂度
        start, end = 0, kth - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1


"""
倍增法O(logk), binary search O(logk), 总体用时O(logk)
"""

