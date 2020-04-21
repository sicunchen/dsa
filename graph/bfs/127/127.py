# https://leetcode.com/problems/word-ladder/


class Solution:
    def ladderLength(self, start, end, dict):
        # write your code here
        wordSet = set(dict)
        if end not in wordSet:
            return 0
        wordSet.add(end)
        queue = collections.deque([start])
        distance = {start: 1}

        while queue:
            word = queue.popleft()
            if word == end:
                return distance[word]
            for next_word in self.get_next_words(word):
                if next_word not in wordSet or next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1
        return 0

    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1 :]
            for char in "abcdefghijklmnopqrstuvwxyz":
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words


"""
Treat each word as a vertex and link it to other words if one can be tranformed to another in only one edit. Then the problem became an graph problem - find the shortest path between two vertices.

Basically a level-order bfs.

代码风格问题：为什么检查next_word的时候用continue而不是直接用valid条件进入queue和visited的操作？？

答： 如果是第二种情况，代码缩进会增加，可读性减弱。
```
for next_word in self.get_next_words(word):
		if next_word in dict:
				if next_word not in visited:
						queue.append(next_word)
						visited.add(next_word)
```
以上代码有三层缩进，对比答案的写法可读性差了很多：
```
for next_word in self.get_next_words(word):
		#异常检测
		if next_word not in dict:
				continue
		if next_word in visited:
				continue
		#正常处理
		queue.append(next_word)
		visited.add(next_word)
```
好的代码习惯写函数是先写异常检测，再写正常处理，减少bug, 增强可读性。


How to get next words? (get a word's neighbors)
Method 1: 
```
for word in dict:
		check word and currentWord's edit distance:
				if distance==1:
						add word to the neighbor list
```
Time: N words in the dict and the avg word length is L.
O(N*L): N=40000, L-10=>400000

Method 2:
```
for char in currentWord: #hot, O(L) time
		for char' in [a-z]: #h - > l
				change char to char'
				make a newWord #lot, O(L) time
				check newWord in dict or not #check lot in dict
```
Time: O(25*L^2): L=10 =>2500<<<400000
"""

