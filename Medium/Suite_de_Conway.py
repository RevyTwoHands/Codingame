r = input()
l = int(input())

conway = [r]
if l > 1:
    for i in range(l):
        cpt = 0
        result = ''
        line = conway[i].split()
        previous = line[0]
        for j, e in enumerate(line):

            if e != previous:
                result += f' {cpt} {previous}'
                previous = e
                cpt = 1
            elif e == previous:
                cpt += 1
            if j == len(line)-1:
                result += f' {cpt} {previous}'
        conway.append(result)

print(conway[l-1].strip())