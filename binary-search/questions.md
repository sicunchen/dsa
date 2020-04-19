https://www.jiuzhang.com/tutorial/algorithm/329

1.  为什么要用 start + 1 < end？而不是 start < end 或者 start <= end?

    为了避免死循环。二分法的模板中，整个程序架构分为两个部分：

    通过 while 循环，将区间范围从 n 缩小到 2 （只有 start 和 end 两个点)。在 start 和 end 中判断是否有解。start < end 或者 start <= end 在寻找目标最后一次出现的位置的时候，可能会出现死循环。

2.  为什么明明可以 start = mid + 1 偏偏要写成 start = mid?

    大部分时候，mid 是可以 +1 和 -1 的。在一些特殊情况下，比如寻找目标的最后一次出现的位置时，当 target 与 nums[mid] 相等的时候，是不能够使用 mid + 1 或者 mid - 1 的。因为会导致漏掉解。那么为了节省脑力，统一写成 start = mid / end = mid 并不会造成任何解的丢失，并且也不会损失效率——log(n) 和 log(n+1) 没有区别。

    ̦
