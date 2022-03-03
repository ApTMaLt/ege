# Для какого наименьшего целого неотрицательного числа A выражение
# (3x + 4y ≠ 70) ∨ (A > x) ∨ (A > y)
# тождественно истинно при любых целых неотрицательных x и y?
for A in range(1000):
    ok = 1
    for x in range(1000):
        for y in range(1000):
            ok *= (3*x + 4*y != 70) or (A > x) or (A > y)
            if not(ok):
                break
    if ok:
        print(A)
        break