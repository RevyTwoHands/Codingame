n = int(input())
y_list = []
x_list = []
for i in range(n):
    house = [int(j) for j in input().split()]
    x_list.append(house[0])
    y_list.append(house[1])

y_list = sorted(y_list)
x_list = sorted(x_list)

med = y_list[n//2]
if n%2 == 0:
    med = (med + y_list[n//2 - 1])//2

x_lenght = x_list[-1]- x_list[0]
y_lenght = sum(abs(y - med) for y in y_list)

print(x_lenght + y_lenght)