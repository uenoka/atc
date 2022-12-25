s = input()
stack = {}
for c in s:
    if c == ')':
        stack = {}
    elif c == '(':
        continue
    else:
        if c in stack:
            print('No')
            exit()
        else:
            stack[c] = 1
print('Yes')
