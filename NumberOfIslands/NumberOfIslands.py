def bfs(x,y,grid,m,n):
    queue = [[x,y]]
    while(len(queue)!=0):
        pop = queue.pop(0)
        i,j = pop[0],pop[1]
        grid[i][j]=0
        
        if i+1<m and grid[i+1][j]==1:
            queue.append([i+1,j])
            grid[i+1][j]=0
            
        if j+1<n and grid[i][j+1]==1:
            queue.append([i,j+1])
            grid[i][j+1]=0
            
        if i>0 and grid[i-1][j]==1:
            queue.append([i-1,j])
            grid[i-1][j]=0
            
        if j>0 and grid[i][j-1]==1:
            queue.append([i,j-1])
            grid[i][j-1]=0

        
# Implement your solution by completing the below function
def numIslands(grid):
    x = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==1:
                x+=1
                bfs(i,j,grid,len(grid),len(grid[0]))
    return x

if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    m = int(row[1])
    grid = []
    for i in range(n):
        r = input()
        grid.append([int(i) for i in r])
    if m==0:
        result=0
    else:
        result = numIslands(grid)
    print(result)
