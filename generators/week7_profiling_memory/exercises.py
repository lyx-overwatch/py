def expensive_calc(n: int) -> int:
    total = 0
    for i in range(n):
        for j in range(i):
            total += (i * j) % (i + 1)
    return total
