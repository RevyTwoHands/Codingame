import re

n = int(input())
txt = '\n'.join(input() for _ in range(n))
pattern = '\(([^(]*)\)'

for pos, match in enumerate(re.findall(pattern, txt)):
    choices = match.split('|')
    txt = txt.replace(f'({match}', choices[pos % len(choices)], 1)

print(txt)









#
# import re
#
# def repl(match):
#     repl.counter += 1
#     choices = match[1].split("|")
#     return choices[repl.counter % len(choices)]
#
# repl.counter = -1
#
# print(''.join(re.sub("\(([^(]*)\)", repl, "".join(f"{input()}\n" for _ in range(int(input()))))))