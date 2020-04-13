https://leetcode.com/problems/contiguous-array/

## Solution 1: Hashtable

Initialize a sum variable=0, decrement by one when 0 is encountered and increment by one when 1 encountered. Also initialize a result varialble=0.There are two situations to consider when traversing the array:

1. The sum becomes zero, update the result with current index+1.

2) When the same sum accumulated at index i appears again at index j, which means there are equal number of 1s and 0s between [i+1, j]. And since we're asked to return the longest subarray, we can use a hashtable to keep track of the **first** index at which the sum appeared. The result would be the larger between previous result and j-i.

Time: O(N)  
Space: O(N)
