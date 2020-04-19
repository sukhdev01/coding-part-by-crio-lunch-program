def myAtoi(s):
    x = 0
    y = 1
    i = len(s) -1
    sign = int(0)
    while i >= 0 and s[i] == " ":
        i = i -1 
    while i >= 0:

        if s[i] in ["1","2","3","4","5","6","7","8","9","0"]:
            x = x + int(s[i]) * y
            y = y *10
            i = i -1
        elif s[i] == '+' or s[i] == ' ':
            i = int(-1)
        elif s[i] == '-':
            sign = 1
            i = int(-1)
    if sign == 1:
        x = x * -1    
    return x

if __name__ == '__main__':
    s = input()
    result = myAtoi(s)
    print(result)