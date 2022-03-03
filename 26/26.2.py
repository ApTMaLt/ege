file = open("26.2.txt").readlines()
a = file[0].replace('\n', '')
a1, a2 = a.split()[0], a.split()[1]
file = file[1:]
b = []
for i in file:
    b.append(int(i.replace('\n', '')))
b.sort()
m = 0
c = 0
print(b)
print(a1)
print(a2)
s = 0
for i in range(int(a2)):
    if m + b[i] < int(a1):
        m += b[i]
        s = b[i]
        c = i + 1
print(c, s)