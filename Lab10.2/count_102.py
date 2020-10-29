def count_letters(s):
    if s:
        return 1 + count_letters(s[1:])
    else:
        return 0
