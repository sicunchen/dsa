https://leetcode.com/problems/majority-element/

##Solution 1: 1-pass hashmap
Build a hashmap that maps elements to appearance counts. As we build the hashmap, if we find an element with a frequency >n/2, we return that element.

**Time**: O(n)
**Space**: O(n)

## Solution 2: sorting

If the elements are sorted in increasing (or descreasing) order, the majority element could be found at [n/2] index.

**Time**: O(nlgn)
**Space**: O(1) (sort in-place)

## Solution 3: Boyer-Moore voting algorithm

http://www.cs.utexas.edu/~moore/best-ideas/mjrty/

https://leetcode.com/problems/majority-element/solution/

What makes an element a majority element? If we keep a count(increment if the number is equal to major else decrement), then an array that starts with this majority element will have a sum > 0. If the count hits 0 it means this subarray doesn't have a majority element. The goal is to find a subarray that starts with a candidate and doesn't hit 0 in the end. That starting element is the majority element we're looking for.

**Time**: O(n)
**Space**: O(1)
