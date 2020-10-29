from sys import stdin

if (__name__ == "__main__"):
    words = [line.strip() for line in stdin]
    offset = 1 if len(words) % 2 else 2
    type_fixer = (lambda a: [a]) if len(words) else (lambda a: a)
    while offset < len(words):
        words = words[:-(offset + 1)] + words[-offset:] + type_fixer(words[-(offset + 1)])
        offset += 2
    print("\n".join(words))
