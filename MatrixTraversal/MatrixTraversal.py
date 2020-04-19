# from crio.python.io import PrintMatrix

# Implement your solution by completing the below function
def traversalPath(matrix, X, Y, dirToMove, stepsToMove):
    res = []
    if X>=len(matrix) or Y>=len(matrix[0]) or X<0 or Y<0 :
        return [-1]
    step=0
    if  (dirToMove <0 or dirToMove > 4):
        return [-1]
    while(step < stepsToMove):
        if dirToMove == 1:
            Y += 1 
        elif dirToMove == 2:
            X += 1 
        elif dirToMove == 3:
            Y -= 1
        else: 
            X -= 1

        if (X<len(matrix) and Y<len(matrix[0]) and X>=0 and Y>=0):
            res.append(matrix[X][Y])
        else:
            return [-1]
        step += 1

    if step == stepsToMove:
        return res
    else:
        return [-1]

if __name__ == '__main__':
    row = input().split()
    n = int(row[0])
    m = int(row[1])
    grid = []
    for i in range(n):
        nums = input().split()
        nums = [int(i) for i in nums]
        grid.append(nums)

    position = input().split()
    currPosX = int(position[0])
    currPosY = int(position[1])
    move = input().split()
    dirToMove = int(move[0])
    stepsToMove = int(move[1])
        
    result = traversalPath(grid, currPosX, currPosY, dirToMove, stepsToMove)
    # PrintMatrix.OneDMatrix(result, " ")
    for i in result:
        print(i,end=' ')
    
