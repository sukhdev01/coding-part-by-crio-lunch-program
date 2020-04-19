def spiralOrder(m, n, mat) :
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


if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    m = int(row[1])
    grid = []
    for i in range(n):
        nums = input().split()
        nums = [int(i) for i in nums]
        grid.append(nums)
    if m > 0 and n > 0:
        result = spiralOrder(n, m, grid)
    for i in range(len(result)):
        print(result[i], end=" ")