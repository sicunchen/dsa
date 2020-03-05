https://leetcode.com/problems/most-common-word/

1. Replace all the punctuations in the paragraph
2. Lowercase all the words
3. Count each word's freq
4. Initialize a maxFreq=0, result="". Loop thru the counter object, if the current word is not in the banned set and its freq is bigger than the maxFreq, then result is the current word.

Time: 0(n)
Space: O(n)
