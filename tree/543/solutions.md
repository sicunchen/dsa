https://leetcode.com/problems/diameter-of-binary-tree/

https://www.youtube.com/watch?v=ey7DYc9OANo

First you need to consider the situation where the longest path passes thru the root:
diameter=leftSubHeight+rightSubHeight

And then you also need to consider the other situation where the longest path does not pass thru the root:
diameter=max(leftSubTreeDiameter, rightSubTreeDiameter)

In conclusion, result=max(leftSubHeight+rightSubHeight, max(leftSubTreeDiameter, rightSubTreeDiameter))

Time: O(n)  
Space: O(n)
