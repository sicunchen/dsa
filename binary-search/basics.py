# find any position: https://www.lintcode.com/problem/classical-binary-search/
def findPosition(self, nums, target):
    if len(nums) == 0 or nums == None:
        return -1
    start = 0
    end = len(nums) - 1

    if target < nums[start] or target > nums[end]:
        return -1

    # key point 1: start + 1 < end
    while start + 1 < end:
        # key point 2: mid = start + Math.floor((end-start)/2)
        mid = start + (end - start) // 2
        # key point 3: separately discuss =, <, >, do not modify start or end as mid + 1 or mid -1
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start = mid
        else:
            end = mid
    # key point 4: after the loop, separately process start and end pointer
    if target == nums[end]:
        return end
    elif target == nums[start]:
        return start

    return -1


# find the first index of the target: https://www.lintcode.com/problem/first-position-of-target/description
def findFirst(self, nums, target):
    # write your code here
    if len(nums) == 0 or nums == None:
        return -1
    start = 0
    end = len(nums) - 1

    if target < nums[start] or target > nums[end]:
        return -1

    while start + 1 < end:
        mid = start + (end - start) // 2
        if target == nums[mid]:
            # 注意可能出现多次，所以当找到这个数字的时候不能直接结束，而要将end移动到mid处。
            # 如果是找其中一个数就可以。如果是找第一个出现或者最后一个出现就不行，得考虑应该是往左找还是往右找
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
    while start + 1 < end:
        mid = start + (end - start) // 2
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
        mid = start + (end - start) // 2
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
        mid = start + (end - start) // 2
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
