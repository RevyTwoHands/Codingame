h = int(input())
array = [list(map(int,input().split())) for i in range(h)]
if len(set(sum(row) for row in array)) > 1:
    print("INVALID")
else:
    for row in array:
        black = [True,False][row[0]!='0']
        for element in row:
            print(element * ['.','O'][black], end="")
            black = not black
        print()
