file = open("24.4.txt").read()
print(file)
a = []
for i in range(len(file)):
    if file[i] == 'A':
        a.append(file[i + 1])
for i in range(ord('A'), ord('Z') + 1):
    print(chr(i), a.count(chr(i)))
