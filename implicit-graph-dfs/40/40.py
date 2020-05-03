# https://leetcode.com/problems/combination-sum-ii/


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ans, tmp, use = [], [], [0] * len(candidates)
        self.dfs(candidates, target, 0, 0, tmp, use)
        return self.ans

    def dfs(self, candidate, target, index, curr, tmp, use):
        if curr == target:
            self.ans.append(tmp[:])
            return
        for i in range(index, len(candidate)):
            if curr + candidate[i] <= target and (
                i == 0 or candidate[i] != candidate[i - 1] or use[i - 1] == 1
            ):
                tmp.append(candidate[i])
                use[i] = 1
                self.dfs(candidate, target, i + 1, curr + candidate[i], tmp, use)
                tmp.pop()
                use[i] = 0

