number = int(input())
d = int(input())

ans = 0

if number % d == 0:
    ans = number
s = str(number)

for i in range(len(str(number))):
    var = int(s[0:i] + s[i + 1:])
    if int(var) % d == 0 and var > ans:
        ans = var
    else:
        for j in range(len(str(var))):
            s2 = str(var)
            var2 = int(s2[0:j] + s2[j + 1:])
            if int(var2) % d == 0 and var > ans:
                ans = var2

print(ans)