# https://leetcode.com/problems/word-ladder-ii/


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        wordSet.add(beginWord)
        wordSet.add(endWord)
        distance = {}
        self.bfs(endWord, distance, wordSet)
        results = []
        self.dfs(beginWord, endWord, distance, wordSet, [beginWord], results)
        return results

    def bfs(self, start, distance, dict):
        distance[start] = 0
        queue = deque([start])
        while queue:
            word = queue.popleft()
            for next_word in self.get_next_words(word, dict):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    queue.append(next_word)

    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i] + c + word[i + 1 :]
                if next_word != word and next_word in dict:
                    words.append(next_word)
        return words

    def dfs(self, curt, target, distance, dict, path, results):
        if curt == target:
            results.append(list(path))
            return
        for word in self.get_next_words(curt, dict):
            if distance[word] != distance[curt] - 1:
                continue
            path.append(word)
            self.dfs(word, target, distance, dict, path, results)
            path.pop()
