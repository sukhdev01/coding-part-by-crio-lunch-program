from crio.python.io import PrintMatrix

# Implement your solution by completing the below function
def twoSum(nums, target):
    v = [0, 0]
    length=len(nums)
    for i in range(length-1):
        for j in range(i+1,length):
            if nums[i]+nums[j]==target:
                return [i,j]
    return v

if __name__ == '__main__':
    n = int(input())
    nums = input().split()
    nums = [int(i) for i in nums]
    target = int(input())
    result = twoSum(nums, target)
    PrintMatrix.OneDMatrix(result, " ")
    
