from sys import stdin

if (__name__ == "__main__"):
    qnou = [
        word.strip() for word in stdin
        if any(
            c.lower() == "q" and word[i + 1].lower() != "u"
            for i, c in enumerate(word)
        )
    ]
    print("Words with q but no u:", qnou)
