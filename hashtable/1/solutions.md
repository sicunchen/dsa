https://leetcode.com/problems/two-sum/

Loop thru the nums array, if target-num already exists in the holder object(numToIndex), immediately return [(target-num)'s index, currentIndex]. Else keep adding num and its index to the holder object.

Time: O(n)
Space: O(n)
