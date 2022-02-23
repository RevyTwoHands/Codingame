vmin = 1
vmax = 100
cheated = False
r = int(input())

for i in range(r):
    nb, _, ans = input().split()
    nb = int(nb)
    if ans == "high":
        vmax = min(vmax, nb - 1)
    elif ans == "low":
        vmin = max(vmin, nb + 1)
    if vmin > vmax or ans == "on" and not vmin <= nb <= vmax:
        print("Alice cheated in round {0}".format(i + 1))
        cheated = True
        break

if not cheated:
    print("No evidence of cheating")
