opened = True
depth = 0
score = {}

for c in input():
    if c == '-':
        opened = False
    elif opened:
        depth += 1
    else:
        score[c] = score.get(c, 0) + 1 / depth
        # dict.get(key, default = None) Si la clé n'a pas de valeur, lui associe default
        depth -= 1
        opened = True

print(max(score, key=score.get))


