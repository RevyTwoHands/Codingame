# Without using datetime

leap = lambda x: x % 400 == 0 or x % 4 == 0 and x % 100 != 0

d1, m1, y1 = map(int, input().split('.'))
d2, m2, y2 = map(int, input().split('.'))

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d3 = 0
y3 = y2 - y1
m3 = m2 - m1
if m3 < 0:
    y3 -= 1
    m3 %= 12
if d2 - d1 < 0:
    m3 -= 1

while (d1, m1, y1) != (d2, m2, y2):
    maxDays = months[m1 - 1]
    if leap(y1) and m1 == 2:
        maxDays = 29
    if d1 <= maxDays:
        d1 += 1
        d3 += 1
    else:
        m1 += 1
        d1 = 1
    if m1 > 12:
        m1 = 1
        y1 += 1

if y3 > 0:
    print(str(y3), ['years', 'year'][y3 == 1], end=', ')
if m3 > 0:
    print(str(m3), ['months', 'month'][m3 == 1], end=', ')
print('total', str(d3), ['days', 'day'][d3 == 1])
