width = int(input())
height = int(input())
text = input().upper()

for i in range(height):
    result = ''
    row = input()
    for e in text:
        if not e.isalpha():  # So it's "?"
            result += row[26 * width:]
        else:
            x = (ord(e) - 65) * width
            result += row[x:x + width]
    print(result)
