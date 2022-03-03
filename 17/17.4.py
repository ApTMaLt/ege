file = open("17.4.txt").readlines()
n = 0
m = 0
a = -6

for i in range(len(file)):
    for j in range(i + 1, len(file)):
        if abs(int(file[i].replace('\n', '')) - int(file[j].replace('\n', ''))) % 2 == 0:
            if int(file[i].replace('\n', '')) % 31 == 0 or int(file[j].replace('\n', '')) % 31 == 0:
                print(file[i].replace('\n', '') + ' ' + file[j].replace('\n', ''))
                n += 1
                if int(file[i].replace('\n', '')) + int(file[j].replace('\n', '')) > m:
                    m = int(file[i].replace('\n', '')) + int(file[j].replace('\n', ''))
print(n, m)
