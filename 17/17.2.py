file = open("17.2.txt").readlines()
n = 0
m = 0
for i in range(len(file)):
    for j in range(i + 1, len(file)):
        a = (int(file[i].replace('\n', '')) - int(file[j].replace('\n', ''))) % 2
        if (int(file[i].replace('\n', '')) - int(file[j].replace('\n', ''))) % 2 == 0:
            if int(file[i].replace('\n', '')) % 19 == 0 or int(file[j].replace('\n', '')) % 19 == 0:
                print(file[i].replace('\n', '') + ' ' + file[j].replace('\n', ''))
                n += 1
                if int(file[i].replace('\n', '')) + int(file[j].replace('\n', '')) > m:
                    m = int(file[i].replace('\n', '')) + int(file[j].replace('\n', ''))
print(n, m)

