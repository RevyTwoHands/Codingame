def buzzle(nb, j, base=10):
    convertedNumber = convert(nb, base)
    sumdigit = sum(int(e) for e in convertedNumber)
    if nb%j == 0:
        return True
    elif int(convertedNumber[-1]) == j:
        return True
    else:
        if len(convertedNumber) > 1:
            return buzzle(sumdigit, j, base)
        else:
            return False


def add(array, index, base):
    if index == len(array):
        array.append(0)
    if array[index] == base - 1:
        array[index] = 0
        add(array, index+1, base)
    else:
        array[index] += 1


def convert(number, base):
    array = [0]
    for i in range(1, number + 1):
        add(array, 0, base)
    return array[::-1]


n, a, b = [int(i) for i in input().split()]
k = int(input())
buzzlers = [int(i) for i in input().split()]

for i in range (a,b+1):
    isBuzzle = False
    for e in buzzlers:
        if buzzle(i, e, n) == True:
            isBuzzle = True
    print([i, "Buzzle"][isBuzzle])