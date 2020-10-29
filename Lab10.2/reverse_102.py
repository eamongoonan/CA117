def reverse_list(lis):
    if lis:
        return [lis.pop()] + reverse_list(lis)
    else:
        return []
