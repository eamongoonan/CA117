import sys

def plural(noun):
    if noun[-1] in "xszo":
        return noun + "es"

    if noun[-2:] in ["ch", "sh"]:
        return noun + "es"

    if noun[-1] == "y" and noun[-2] not in "aeiou":
        return noun[:-1] + "ies"

    if noun[-2:] == "fe":
        return noun[:-2] + "ves"
    if noun[-1] == "f":
        return noun[:-1] + "ves"

    return noun + "s"

if (__name__ == "__main__"):
    [print(plural(line.strip())) for line in sys.stdin]
