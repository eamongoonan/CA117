def sumup(n):
    if 0 < n:
        return n + sumup(n - 1)
    else:
        return 0
