from sys import stdin

def num_to_word(i):
    under_20 = [
        "zero", "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"
    ]

    tens = {
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
    }

    if (i == 100):
        return "one hundred"
    elif (i < 20):
        return under_20[i]
    else:
        words = []
        words.append(tens[i - i % 10])
        if i % 10 != 0:
            words.append(under_20[i % 10])

    return "-".join(words)

if (__name__ == "__main__"):
    for line in stdin:
        print(" ".join([
            num_to_word(int(num))
            for num in line.strip().split()
        ]))
