file = open("26.1.txt").readlines()
n = 0
m = 0
for i in range(1, int(file[0]) + 1):
    if int(file[i].replace('\n', '')) % 2 != 0:
        for j in range(i + 1, int(file[0]) + 1):
            if int(file[j].replace('\n', '')) % 2 != 0:
                gg = (int(file[i].replace('\n', '')) + int(file[j].replace('\n', ''))) // 2
                vv = file.count(str(gg) + '\n')
                if file.count(str(gg) + '\n') == 1:
                    n += 1
                    print(gg)
                    if gg > m:
                        m = gg

print(n, m)
