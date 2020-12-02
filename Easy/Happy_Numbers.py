def is_happy(x):
    previous_values = [1]

    while x not in previous_values:
        previous_values.append(x)
        x = sum(int(e) ** 2 for e in str(x))
    return x == 1


n = int(input())
for i in range(n):
    x = input()
    print(x, ':)' if is_happy(int(x)) else ':(')
