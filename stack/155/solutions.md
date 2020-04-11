https://leetcode.com/problems/min-stack/

## Solution 1: one-stack solution

The idea is to add current element and current minimum element as a tuple (or array) onto the stack so we can get the min element in constant time.

Time: O(1)  
Space: O(N)

## Solution 2: linked list

Similar to the 1st solution, we keep track of the current minimum element by building a linked list backwards. The minimum val will always be the value of the head node.

Time: O(1)  
Space: O(N)

## Solution 3: two stacks

Add another minimum tracker stack to track the current minimum element. Only if the current element is smaller OR EQUAL to the current minimum element does it get added to the minimum tracker stack.

Time: O(1)  
Space: O(N)
