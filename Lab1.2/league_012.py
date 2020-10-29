from sys import stdin

class fmt:
    def __init__(self, heading, just=">", exws=2):
        self.heading = heading
        self.just = just
        self.exws = exws * " "

    heading = ""
    just = ""
    exws = ""

def tokenize(words):
    return [words[0]] + [" ".join(words[1:-8])] + words[-8:]

def table(data, fmts):
    cols = [len(fmt.heading) for fmt in fmts]
    for i in range(len(cols)):
        max_dlen = len(max([line[i] for line in data], key=len))
        cols[i] = max_dlen if cols[i] < max_dlen else cols[i]

    print("".join([
        "{:{}{}}".format(fmts[i].heading, fmts[i].just, cols[i]) +
        fmts[i].exws
        for i in range(len(cols))
    ]))

    for line in data:
        print("".join([
            "{:{}{}}".format(line[i], fmts[i].just, cols[i]) +
            fmts[i].exws
            for i in range(len(cols))
        ]))

if (__name__ == "__main__"):
    table(
        [tokenize(line.strip().split()) for line in stdin],
        [fmt(*arg) for arg in [
            ("POS", ">", 1),
            ("CLUB", "<", 1),
            ("P",),
            ("W",),
            (" D",),
            ("L",),
            ("GF",),
            ("GA", ">", 1),
            ("GD", ">", 1),
            ("PTS", ">", 0)
        ]]
    )
