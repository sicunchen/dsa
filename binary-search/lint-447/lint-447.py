class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):
        # write your code here
        start = 0
        index = 1
        while reader.get(index) < target:
            index = index * 2

        # now we have un upper bound
        start, end = index // 2, index

        while start + 1 < end:
            mid = start + (end - start) // 2
            if target <= reader.get(mid):
                end = mid
            else:
                start = mid

        # find the first position of the target in the search space
        if reader.get(start) == target:
            return start
        elif reader.get(end) == target:
            return end
        return -1

        # 老师的写法：

    def searchBigSortedArray1(self, reader, target):
        kth = 1
        while reader.get(kth - 1) < target:
            kth = kth * 2

        # start 也可以是 kth // 2，但是我习惯比较保守的写法
        # 因为写为 0 也不会影响时间复杂度
        start, end = 0, kth - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
