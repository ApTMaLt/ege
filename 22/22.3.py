
for x in range(1000):
    k = x
    L = 0
    M = 0
    while x > 0:
        L = L + 1
        if M < x:
            M = M + (x % 10) * 2
        x = x // 10
    if L == 3 and M == 28:
        print(L, M, k)