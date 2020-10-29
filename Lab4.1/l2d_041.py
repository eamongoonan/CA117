def l2d(file):
    keys = file.readline().strip().split()
    vals = file.readline().strip().split()
    return dict(zip(keys, vals))
