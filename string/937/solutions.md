https://leetcode.com/problems/reorder-data-in-log-files/

basically just translate these rules into a comparator function;

1. letter-logs come before digit-logs
2. letter-logs are sorted lexicographically by content first and then identifier if there's a tie
3. digit-logs remain the original order

Time: O(nlogn)
Space: O(n)
