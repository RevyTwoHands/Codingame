# Converting ASCII Characters into binary
message = input()
message = [bin(ord(e))[2:].zfill(7) for e in message]
message = ''.join(message)


previous = ''
answer = ''

for e in message:
    if e == '1' != previous:
        answer += ' 0 0'
    elif e == '0' != previous:
        answer += ' 00 0'
    else:
        answer += '0'

    previous = e

print(answer.strip())
