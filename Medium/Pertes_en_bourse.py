n = int(input())

loss = 0
max_price = 0

for price in list(map(int, input().split())):
    max_price = max(price, max_price)
    loss = max(loss, max_price - price)
print(-loss)