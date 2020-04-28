class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rowCount,colCount=len(grid),len(grid[0])
        fresh=0
        rotten=collections.deque()
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    rotten.append((j,i))
        mins=0
        while fresh!=0 and rotten:
            size=len(rotten)
            for o in range(size):                
                x,y=rotten.popleft()
                if x-1>=0 and grid[y][x-1]==1:
                    grid[y][x-1]=2
                    rotten.append((x-1,y))
                    fresh-=1
                if x+1<colCount and grid[y][x+1]==1:
                    grid[y][x+1]=2
                    rotten.append((x+1,y))
                    fresh-=1
                if y+1<rowCount and grid[y+1][x]==1:
                    grid[y+1][x]=2
                    rotten.append((x,y+1))
                    fresh-=1
                if y-1>=0 and grid[y-1][x]==1:
                    grid[y-1][x]=2
                    rotten.append((x,y-1))
                    fresh-=1
            mins+=1
        
        return mins if fresh==0 else -1
            