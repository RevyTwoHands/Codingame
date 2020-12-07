import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
table = {}

for i in range(int(input())):
    b, c = input().split()
    table[b] = chr(int(c))

s = input()

result = ''
buffer = ''

for i, c in enumerate(s):
    buffer += c
    if buffer in table:
        result += table[buffer]
        buffer = ""

print(result if not buffer else f"DECODE FAIL AT INDEX {i - len(buffer) + 1}")
