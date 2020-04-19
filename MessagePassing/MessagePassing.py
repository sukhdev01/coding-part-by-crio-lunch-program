def spiralOrder(m, n, mat):
    k = 0; l = 0
    res = []
    while (k < m and l < n) :
        for i in range(l, n) :
            res.append(mat[k][i])
        k += 1
        for i in range(k, m) :
            res.append(mat[i][n-1])
        n -= 1
        if ( k < m) :
            for i in range(n - 1, (l - 1), -1) :
                res.append(mat[m-1][i])
        m -= 1
        if (l < n) :
            for i in range(m - 1, k - 1, -1) :
                res.append(mat[i][l])
        l += 1
    return res
# Implement your solution by completing the below function
def canMessageBePassed(n, maze):
    res = True
    ans = spiralOrder(n,n,maze)
    i=0
    strength = ans[0]
    while(i<n*n):
        array=[]
        for j in range(i+1,strength+1):
            if j<n*n and ans[j]!=0:
                array.append([j,ans[j],j+ans[j]])
        if j >= n*n -1:
            return True
        elif len(array)==0:
            return False
        else:
            maxx = 0
            index = 0
            for t in range(len(array)):
                if array[t][2] > maxx:
                    index = t
                    maxx = array[t][2]
            i=array[index][0]
            strength = array[index][2]  
    return res

if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    s = int(row[1])
    m = int(row[2])
    
    maze = [[0 for col in range(n)] for row in range(n)]
    maze[0][0] = s

    for i in range(m):
        perPersonInput = input().split()
        x = int(perPersonInput[0])
        y = int(perPersonInput[1])
        p = int(perPersonInput[2])
        maze[x][y] = max(maze[x][y],p)
    result = canMessageBePassed(n, maze)
    if (result == True):
        print ("Yes")
    else:
        print ("No")
