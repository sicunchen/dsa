https://leetcode.com/problems/valid-parentheses/

If an input string is stripped of all the valid substrings, it would be empty. We can use a stack to keep track of the smallest valid substrings.

1. Initialize a stack
2. Loop thru the input string, check if the top element of the stack is the match of the current bracket. If they do match then pop off the top element (remove a valid substring from the input string), else push the current bracket on the stack.
3. If the stack is empty at the end it means the whole input string is valid, else invalid.
