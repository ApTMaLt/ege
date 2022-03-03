file = open("24_demo.txt").read()
m = 0
c = 1
for i in range(len(file)-1):
    a = file[i]
    b = file[i+1]
    if file[i] != file[i+1]:
        c += 1
    else:
        if c > m:
            m = c
        c = 1
print(m)