from collections import deque
def BFS(grid,startX,startY,goalX,goalY):
    n=len(grid)
    visited=[[False]*n for _ in range(n)]
    queue=deque([(startX,startY,0)])
    visited[startX][startY]=True
    while queue:
        x,y, moves=queue.popleft()
        if x==goalX and y==goalY:
            return moves
        for i in range(x-1,-1,-1):
            if grid[i][y]==1:
                break
            if not visited[i][y]:
                visited[i][y]=True
                queue.append((i,y,moves+1))
        for i in range(x+1,n):
            if grid[i][y]==1:
                break
            if not visited[i][y]:
                visited[i][y]=True
                queue.append((i,y,moves+1))
        for i in range(y-1,-1,-1):
            if grid[x][i]==1:
                break
            if not visited[x][i]:
                visited[x][i]=True
                queue.append((x,i,moves+1))
    return -1
if __name__=="__main__":
    n = int(input("Enter the size of the grid: "))
    grid = [input().strip() for _ in range(n)]  
    startX, startY, goalX, goalY = map(int, input("Enter startX startY goalX goalY: ").split())
    result = BFS(grid, startX, startY, goalX, goalY)
    print("Minimum moves:", result)
