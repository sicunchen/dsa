https://leetcode.com/problems/rotting-oranges/

Start from all the rotten oranges(source vertex), see if the fresh oranges could be infected level by level(BFS). If yes, return the distance between source vertex and the last vertex visited. If not(there're still fresh oranges left untouched) return -1.
