https://leetcode.com/problems/valid-palindrome/

Keep two pointers start and end, if the character at start or end pointer is not alphanumeric, skip the current character(start++ or end--). If they're both alphanumeric, check if they share the same value, if not immediately return false.
