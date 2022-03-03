file = open("24.3.txt").read()
file = file.split('\n')
m = 100000
a = []
for i in file:
    c = i.count('N')
    if c < m:
        m = c
        a = i
g = 0
for i in a:
    c = a.count(i)
    if c > g:
        g = c
        gg = i
print(gg)
