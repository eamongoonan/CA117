from sys import stdin

if (__name__ == "__main__"):
    scores = {}
    for line in stdin:
        name, score = line.strip().split(":")
        scores[name] = sum(map(int, score.translate(str.maketrans("X", "0")).strip().split(","))) / 6
    for player, score in sorted(scores.items(), key=lambda a: a[1], reverse=True):
        print("{}: {:.1f}".format(player, score))
