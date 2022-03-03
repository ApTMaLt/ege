# for n in range(1000):
#     q = 0
#     for i in range(1, n):
#         if n % i == 0:
#             q = i
#     if q == 17:
#         print(q, n)

q = 0
n = int(input())
for i in range(1, n):
    if n % i == 0:
        q = i
print(q)