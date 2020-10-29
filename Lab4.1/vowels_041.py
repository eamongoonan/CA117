from sys import stdin

if (__name__ == "__main__"):
    vowels = "aeiou"
    vowel_freq = dict(zip(vowels, [0, 0, 0, 0, 0]))
    for line in stdin:
        for c in vowels:
            vowel_freq[c] += line.lower().count(c)

    vowel_freq = sorted(vowel_freq.items(), key=lambda kv: kv[1], reverse=True)
    max_elem = max(vowel_freq, key=lambda a: len(str(a[1])))
    for pair in vowel_freq:
        print(pair[0], ":", "{:{:d}d}".format(pair[1], len(str(max_elem[1]))))
