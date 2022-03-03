file = open("27-B_2.txt").readlines()
for i in range(1, int(file[0].replace('\n', '')) + 1):
    file[i] = int(file[i].replace('\n', ''))
file = file[1:]
for i in range(5000-1):
    for j in range(5000-i-1):
        if file[j] > file[j+1]:
            file[j], file[j+1] = file[j+1], file[j]
# file.sort()
# for i in range(5000):
#     for j in range(i + 1, 5000):
#         for k in range(j + 1, 5000):
#             if (file[i] + file[j] + file[k]) % 3 == 0:
#                 print(file[i], file[j], file[k], (file[i] + file[j] + file[k]))
print(file)
# a = 8 + 75 + 152
# b = 8 + 75 + 275
# c = 8 + 75 + 316
# d = 75 + 152 + 275
# print(a, b, c,d)