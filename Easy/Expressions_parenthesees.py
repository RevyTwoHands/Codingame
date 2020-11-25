expression = input()
t = []
closing = {'}':'{', ']':'[', ')':'('}
ans='true'
for e in expression:
    if e in '{([':
        t.append(e)
    elif e in '])}' and (not t or t.pop() != closing[e]): # not t means array is empty
        ans='false'
print('false' if t else ans)
