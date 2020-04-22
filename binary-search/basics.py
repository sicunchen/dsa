# find any position: https://www.lintcode.com/problem/classical-binary-search/
def findPosition(self, nums, target):
    if len(nums) == 0 or nums == None:
        return -1
    start = 0
    end = len(nums) - 1

    if target < nums[start] or target > nums[end]:
        return -1

    """
    key point 1: start + 1 < end

    为什么要用 start + 1 < end？而不是 start < end 或者 start <= end?

    为了避免死循环。二分法的模板中，整个程序架构分为两个部分：

    通过 while 循环，将区间范围从 n 缩小到 2 （只有 start 和 end 两个点)。在 start 和 end 中判断是否有解。start < end 或者 start <= end 在寻找目标最后一次出现的位置的时候，可能会出现死循环。样例：nums=[1,1],target=1
    此循环退出后start和end有可能相等（start=end不会进入循环），也有可能相邻（start+1=end)
    """
    while start + 1 < end:
        """
        key point 2: mid = stat + Math.floor((end-start)/2)

        用python可直接用mid=(start+end)//2, java需写成mid=start+(end-start)/2 (整除)
        """
        mid = (start + end) // 2
        """
        key point 3: separately discuss =, <, >, do not modify start or end as mid + 1 or mid -1

        为什么明明可以 start = mid + 1 偏偏要写成 start = mid?

        大部分时候，mid 是可以 +1 和 -1 的。在一些特殊情况下，比如寻找目标的最后一次出现的位置时，当 target 与 nums[mid] 相等的时候，是不能够使用 mid + 1 或者 mid - 1 的。因为会导致漏掉解。那么为了节省脑力，统一写成 start = mid / end = mid 并不会造成任何解的丢失，并且也不会损失效率——log(n) 和 log(n+1) 没有区别。
        """
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid
        else:
            end = mid
    """
    key point 4: after the loop, separately process start and end
    """
    if target == nums[end]:
        return end
    elif target == nums[start]:
        return start

    return -1


# find the first index of the target: https://www.lintcode.com/problem/first-position-of-target/description
def findFirst(self, nums, target):
    if len(nums) == 0 or nums == None:
        return -1
    start = 0
    end = len(nums) - 1

    if target < nums[start] or target > nums[end]:
        return -1

    while start + 1 < end:
        mid = (start + end) // 2
        if target == nums[mid]:
            """
            注意可能出现多次，所以当找到这个数字的时候不能直接结束，而要将start或end移动到mid处。
            如果是找其中一个数就可以。如果是找第一个出现或者最后一个出现就不行，得考虑应该是往左找还是往右找
            这里是找first position, 所以往左走
            """
            end = mid
        elif target > nums[mid]:
            start = mid
        else:
            end = mid
    # 直到最后缩小到只有一个或两个数字时，优先判断start，再判断end。
    if target == nums[start]:
        return start
    elif target == nums[end]:
        return end

    return -1


# https://www.lintcode.com/problem/last-position-of-target/description
def findLast(self, nums, target):
    # write your code here
    if len(nums) == 0 or nums == None:
        return -1

    start = 0
    end = len(nums) - 1

    if target < nums[start] or target > nums[end]:
        return -1
    """
    start < end 或者 start <= end 在寻找目标最后一次出现的位置的时候，可能会出现死循环。样例：nums=[1,1],target=1
    """
    while start + 1 < end:
        mid = (start + end) // 2
        if target == nums[mid]:
            start = mid
        elif target > nums[mid]:
            start = mid
        else:
            end = mid

    if target == nums[end]:
        return end
    elif target == nums[start]:
        return start

    return -1


# https://www.lintcode.com/problem/search-for-a-range/description
# Basically a combination of findFirst and findLast.
def findRange(self, nums, target):
    if len(nums) == 0:
        return [-1, -1]

    # search for left bound
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if target == nums[mid]:
            end = mid
        elif target > nums[mid]:
            start = mid
        else:
            end = mid
    if target == nums[start]:
        first_pos = start
    elif target == nums[end]:
        first_pos = end
    else:
        return [-1, -1]

    # search for right bound
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if target == nums[mid]:
            start = mid
        elif target > nums[mid]:
            start = mid
        else:
            end = mid
    if target == nums[end]:
        last_pos = end
    elif target == nums[start]:
        last_pos = start
    else:
        return [-1, -1]
    return [first_pos, last_pos]
