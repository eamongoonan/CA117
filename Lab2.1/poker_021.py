from sys import stdin

if (__name__ == "__main__"):
    rank_names = [
        "nothing",
        "one pair",
        "two pairs",
        "three of a kind",
        "a straight",
        "a flush",
        "a full house",
        "four of a kind",
        "a straight flush",
        "a royal flush"
    ]

    rank_count = [0 for i in range(10)]
    for line in stdin:
        rank_count[int(line.strip().split(",")[-1])] += 1

    total_hands = sum(rank_count)

    for i in range(10):
        print(
            "The probability of",
            rank_names[i],
            "is",
            "{:.4f}".format((rank_count[i] / total_hands) * 100) + "%"
        )
