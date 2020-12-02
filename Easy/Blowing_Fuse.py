devices_number, total_clicked, max_capacity = [int(i) for i in input().split()]
tab = [int(i) for i in input().split()]

devices_ON = []
max_current = 0
fuse_blown = False

for i in input().split():
    mx = int(i) - 1

    if mx in devices_ON:
        devices_ON.remove(mx)
    else:
        devices_ON.append(mx)

    actual_current = sum(tab[i] for i in devices_ON)
    max_current = max(max_current, actual_current)

    if actual_current > max_capacity:
        fuse_blown = True

if fuse_blown:
    print("Fuse was blown.")
else:
    print("Fuse was not blown.")
    print(f"Maximal consumed current was {max_current} A.")
