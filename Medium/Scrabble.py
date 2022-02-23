# def calcScore(word):
#     res = 0
#     for letter in word:
#         for e in scores:
#             if letter in e:
#                 res += scores.index(e) + 1
#     return res
#
# def wordInLetters(word):
#     for letter in set(word):
#         if letter not in letters:
#             return False
#         else:
#             if word.count(letter) > letters.count(letter):
#                 return False
#     return True
#
# scores = ['e, a, i, o, n, r, t, l, s, u', 'd, g', 'b, c, m, p', 'f, h, v, w, y', 'k','','', 'j, x','','', 'q,z']
#
# n = int(input())
# dictionnaire = [input() for i in range(n)]
# letters = [i for i in input()]
#
# bestWord = ""
# bestScore = 0
#
# for word in dictionnaire:
#     if wordInLetters(word):
#         res = calcScore(word)
#         if res > bestScore:
#             bestScore = res
#             bestWord = word
#
# print(bestWord)


def value(c):
    if c in 'qz': return 10
    if c in 'jx': return 8
    if c in 'k': return 5
    if c in 'fhvwy': return 4
    if c in 'bcmp': return 3
    if c in 'dg': return 2
    return 1

n = int(input())
words = [input() for i in range(n)]
letters = input()

maxsum = 0
for w in words:
    wsum = 0
    for c in w:
        if w.count(c) > letters.count(c):
            wsum = 0
            break
        wsum += value(c)
    if wsum > maxsum:
        maxsum = wsum
        maxsumword = w

print(maxsumword)