from collections import defaultdict
from sys import stdin

def filter(map, key):
    temp = map.copy()
    temp.clear()
    temp.update({kv for kv in map.items() if key(kv)})
    return temp

if (__name__ == "__main__"):
    counts = defaultdict(lambda: 0)
    for line in stdin:
        for token in line.strip().lower().split():
            word = token.translate(str.maketrans(".?,", "   ")).strip()
            counts[word] += 1

    counts = filter(counts, lambda kv: 3 < len(kv[0]) and 2 < kv[1])

    max_word_len = len(max(counts, key=len))
    max_num_len = len(str(max(counts.values(), key=lambda a: len(str(a)))))
    for key in sorted(counts):
        print(
            "{:>{:}}".format(key, max_word_len),
            ":",
            "{:>{:}}".format(counts[key], max_num_len)
        )
