file = open("27-B_2.txt").readlines()
gg = []
for i in range(1, int(file[0]) + 1):
    for j in range(i + 1, int(file[0]) + 1):
        if (int(file[i].replace('\n', '')) * int(file[j].replace('\n', ''))) % 14 == 0:
            gg.append(int(file[i].replace('\n', '')) * int(file[j].replace('\n', '')))
print(max(gg))
print(gg)
print(gg.count(447552))