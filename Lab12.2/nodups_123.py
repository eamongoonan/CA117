from sys import stdin

if (__name__ == "__main__"):
    del_table = str.maketrans({s: "" for s in ".,!?"})
    words = set()
    for line in stdin:
        nodups = []
        for word in line.strip().split():
            if word.lower().translate(del_table) in words:
                nodups.append(".")
            else:
                nodups.append(word)
                words.add(word.lower().translate(del_table))
        print(" ".join(nodups))
