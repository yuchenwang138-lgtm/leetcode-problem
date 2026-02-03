t = int(input())
s_list = []

def solve(s):
    stack = []
    pairs = {')':'(',']':'[','}':'{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return 'No'
            stack.pop()
    return 'Yes' if not stack else 'No'

cur = ""   

for _ in range(t):
    row = input().split()
    if row[0] == '1':  
        if row[1] == '(':
            cur += '('
        elif row[1] == ')':
            cur += ')'
    elif row[0] == '2':  
        if cur:
            cur = cur[:-1]
    s_list.append(cur)

for s in s_list:
    print(solve(s))
