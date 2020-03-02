https://leetcode.com/problems/string-compression/

Maintain two pointers read and write to write in-place.

Use two while loops: the inner loop counts the streak of common charactes.

Always write the character, but only write the frequency when it's more than 1.

Time: O(n)
Space: O(1)
