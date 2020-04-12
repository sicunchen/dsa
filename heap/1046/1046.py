# solution 1
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        def remove_largest():
            largestIndex = stones.index(max(stones))
            stones[-1], stones[largestIndex] = stones[largestIndex], stones[-1]
            return stones.pop()

        while len(stones) > 1:
            stone1 = remove_largest()
            stone2 = remove_largest()
            if stone1 != stone2:
                stones.append(stone1 - stone2)
        return stones[0] if stones else 0


# solution 2 pseudocdoe
# define function last_stone_weight(stones):
#     heap = a new Max-Heap
#     add all stones to heap
#     while heap contains more than 1 stone:
#         heavy_stone_1 = remove max from heap
#         heavy_stone_2 = remove max from heap
#         if heavy_stone_1 is heavier than heavy_stone_2:
#             new_stone = heavy_stone_1 - heavy_stone_2
#             add new_stone to heap
#     if heap is empty:
#         return 0
#     return last stone on heap


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * -1
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)

        return heapq.heappop(stones) * -1 if stones else 0

