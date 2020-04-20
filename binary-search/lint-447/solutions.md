https://www.lintcode.com/problem/search-in-a-big-sorted-array/description

## Solution 1: binary search

Normal binary search needs to know the full array length to start the search. However since this is a huge array we can first "jump" to find an upper bound.

Time: O(logk), k is the first index of the given target number

Space: O(1)
