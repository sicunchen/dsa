"""
这个题 LintCode 和 LeetCode 的 find peak element 是有区别的。
数据上，LintCode 保证数据第一个数比第二个数小，倒数第一个数比到倒数第二个数小。
因此 start, end 的范围要取 1, len(A) - 2

二分法。
每次取中间元素，如果大于左右，则这就是peek。
否则取大的一边，两个都大，可以随便取一边。最终会找到peek。

正确性证明：

A[0] < A[1] && A[n-2] > A[n-1] 所以一定存在一个peek元素。
二分时，选择大的一边, 则留下的部分仍然满足1 的条件，即最两边的元素都小于相邻的元素。所以仍然必然存在peek。
二分至区间足够小，长度为3, 则中间元素就是peek。
"""


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            # 如果mid比mid-1小说明左边有峰，去左边
            if nums[mid] < nums[mid - 1]:
                end = mid
            # 如果mid比mid+1小说明右边有峰，去左边
            elif nums[mid] < nums[mid + 1]:
                start = mid
            # 峰在此
            else:
                return mid

        if nums[start] < nums[end]:
            return end
        else:
            return start
