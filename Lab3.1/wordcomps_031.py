from sys import stdin

def collect(data, key):
    return [elem for elem in data if key(elem)]

def main():
    data = [word.strip() for word in stdin]
    print("Words containing 17 letters:", collect(data, lambda a: len(a) == 17))
    print("Words containing 18+ letters:", collect(data, lambda a: 17 < len(a)))
    print(
        "Shortest word containing all vowels:",
        min(collect(data, lambda a: all([c in a.lower() for c in "aeiou"])), key=len)
    )
    print("Words with 4 a's:", collect(data, lambda a: a.lower().count("a") == 4))
    print("Words with 2+ q's:", collect(data, lambda a: 1 < a.lower().count("q")))
    print("Words containing cie:", collect(data, lambda a: "cie" in a.lower()))
    print(
        "Anagrams of angle:",
        collect(data, lambda a: sorted("angle") == sorted(a.lower()) and not(a == "angle"))
    )
    print(
        "Words ending in iary:",
        len(collect(data, lambda a: a.lower().endswith("iary")))
    )
    coont = max(data, key=lambda a: a.lower().count("e")).count("e")
    print(
        "Words with most e's:",
        [i for i in data if i.count("e") == coont]
    )

if (__name__ == "__main__"):
    main()
