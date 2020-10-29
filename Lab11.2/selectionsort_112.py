def selectionsort(data):
    for i, d in enumerate(data):
        mind = i
        for n in range(i, len(data)):
            mind = n if data[n] < data[mind] else mind
        data[i], data[mind] = data[mind], data[i]
