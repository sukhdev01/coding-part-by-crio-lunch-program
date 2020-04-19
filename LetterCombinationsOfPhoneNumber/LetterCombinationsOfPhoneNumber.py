
from crio.python.io import PrintMatrix

# Implement your solution by completing the below function
hashTable = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def formCombination(res, num):
    newres = []
    for i in range(len(res)):
        for j in range(len(num)):
            newres.append(res[i] + num[j])
    return newres

def letterCombinations(digits):
    i = 0
    res = hashTable[int(digits[i])]
    for i in range(len(digits)-1):
        num = hashTable[int(digits[i+1])]
        res = formCombination(res, num)
    return res

if __name__ == '__main__':
    digits = input()
    letterCombinations(digits)
    result = letterCombinations(digits)
    PrintMatrix.OneDMatrix(result, " ")
