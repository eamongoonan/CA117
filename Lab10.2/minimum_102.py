def minimum(lis, i=0, m=0):
    if i < len(lis):
        m = i if lis[i] < lis[m] else m
        return minimum(lis, i + 1, m)
    else:
        return lis[m]
