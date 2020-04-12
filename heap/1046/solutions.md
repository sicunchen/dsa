https://leetcode.com/problems/last-stone-weight/

## Solution 1: basic array solution

Repeatly search for the 2 largest stones and remove them, and if they are not the same size add the new stone in the array. Repeat the process until there's only one stone left. One way to avoid other stones shuffling when deleting the heavy stones is to simply swap the heavy stone with the last stone and pop them off the array.

Time: The search and remove costs O(N), N is the stones array length. To reduce the stones array size down to one we need to loop up to N-1 times, so in total we need O(N^2).

Space: O(1) in Python

## Solution 2: max-heap

Using a heap data structure could reduce the search-and-remove and add-new-stone operations to O(logN).

Time: O(NlogN)
Space: O(1) in Python
