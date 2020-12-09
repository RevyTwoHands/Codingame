def shift(message, shift, reverse=False):
    result = ''
    if not reverse:
        for i, l in enumerate(message):
            result += chr((ord(l) - ord('A') + shift + i) % 26 + ord('A'))
    else:
        for i, l in enumerate(message):
            result += chr((ord(l) - ord('A') - shift - i) % 26 + ord('A'))
    return result


def encode(message, rotor, reverse=False):
    result = ''
    if not reverse:
        for l in message:
            position = ord(l) - ord('A')
            result += rotor[position]
    else:
        for l in message:
            position = rotor.index(l)
            result += chr(ord('A') + position)
    return result


# --------------------------------------------------------------------------------

operation = input()
pseudo_random_number = int(input())
rotors = [input() for i in range(3)]
message = input()

if operation == 'ENCODE':
    message = shift(message, pseudo_random_number)
    for i in range(3):
        message = encode(message, rotors[i])
else:
    for i in range(2, -1, -1):
        message = encode(message, rotors[i], reverse=True)
    message = shift(message, pseudo_random_number, reverse=True)

print(message)
