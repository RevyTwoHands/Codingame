n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
ext = {}

for i in range(n):
    a,b = input().split()
    ext[a.lower()] = b

for i in range(q):
    fname = input().split('.')
    if len(fname) < 2: # if no extension
        print('UNKNOWN')
    else:
        print(ext.get(fname[-1].lower(), 'UNKNOWN'))