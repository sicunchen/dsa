https://leetcode.com/problems/implement-strstr/

Solution 1: Naive solution
Keep a block of the needle length. Loop thru the haystack and search if the current block matches with the needle.

Time: O((N-M)\*M), M is needle length, N is haystack length.  
Space: O(1)

Solution 2: Rabin - Karp
The searching and comparing part of the naive solution costs O(M). How can we speed up this part? We can turn the substring into an integer using a hash function.

https://www.youtube.com/watch?v=H4VrKHVG5qI

https://www.jiuzhang.com/tutorial/algorithm/318

Time: O(N+M)  
Space: O(1)
