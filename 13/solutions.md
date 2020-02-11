https://leetcode.com/problems/roman-to-integer/

Example: MCM->1900

Solution 1:
If we sum all symbols, the result would be 2M+C, but the correct sum is M+M-C=2M-C. The difference is 2\*(smaller symbol value). So we can ccumulate the value of each letter one by one, if the value of the current letter is greater than the previous one, deduct twice of the previous value.

Solution 2:
As we accumulate the sum, if the current letter's value is smaller than the next value, subtract the current value.

Time complexity: O(N)
Space complexity: O(1)
