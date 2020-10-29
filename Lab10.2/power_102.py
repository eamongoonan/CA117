def power(n, m):
    if 0 < m:
        return n * power(n, m - 1)
    else:
        return 1
