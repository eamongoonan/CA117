def find():
    top = 1000000
    bottom = 0
    while(bottom < top):
        jump = bottom + (top - bottom) // 2
        g = guess(jump)
        if (g == 1):
            top = jump
        elif (g == -1):
            bottom = jump + 1
        else:
            return jump

    return bottom
