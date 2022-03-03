file = open("17.3.txt").readlines()
n = 0
m = 0
s = 0
k = 1
for i in range(len(file)):
    if int(file[i].replace('\n', '')) % 2 != 0:
        s += int(file[i].replace('\n', ''))
        k += 1
gg = s / k
print(gg)
for i in range(len(file)):
    if i + 1 <= len(file) - 1:
        if int(file[i].replace('\n', '')) % 5 == 0 or int(file[i + 1].replace('\n', '')) % 5 == 0:
            if int(file[i].replace('\n', '')) < gg or int(file[i + 1].replace('\n', '')) < gg:
                print(file[i].replace('\n', '') + ' ' + file[i + 1].replace('\n', ''))
                n += 1
                if int(file[i].replace('\n', '')) + int(file[i + 1].replace('\n', '')) > m:
                    m = int(file[i].replace('\n', '')) + int(file[i + 1].replace('\n', ''))
print(n, m)
