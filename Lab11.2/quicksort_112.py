def partition(lst, start, end):
    pos = start
    for i in range(start, end):
        if lst[i] < lst[end]:
            lst[i], lst[pos] = lst[pos], lst[i]
            pos += 1
    lst[pos], lst[end] = lst[end], lst[pos]
    return pos

def quicksort(lst, start, end):
    if start < end:
        pos = partition(lst, start, end)
        quicksort(lst, start, pos - 1)
        quicksort(lst, pos + 1, end)
