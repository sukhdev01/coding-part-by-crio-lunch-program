def isValid(s):
    res = 0
    stack = ["a"]
    if len(s) > 0:
        stack.append(s[0])
    for i in range(1,len(s)):
        ele = stack.pop()
        if ((ele == "(" and s[i] == ")") or (ele == "[" and s[i] == "]") or (ele == "{" and s[i] == "}")):
            a = -1
        else:
            stack.append(ele)
            stack.append(s[i])
    if stack.pop() != "a":
        return 1
    return res

if __name__ == '__main__':
    s = input()
    result = isValid(s)
    if result == 1:
        print('false')
    else:
        print('true')