def maximum(lis, i=0, m=0):
    if i < len(lis):
        m = i if lis[m] < lis[i] else m
        return maximum(lis, i + 1, m)
    else:
        return lis[m]
