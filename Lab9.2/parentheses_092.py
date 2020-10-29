def matcher(string):
    pairs = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    braces = list(string)
    checked = []
    while braces:
        try:
            if checked and pairs[checked[-1]] == braces[-1]:
                braces.pop()
                checked.pop()
            else:
                checked.append(braces.pop())
        except:
            return False
    return len(checked) == 0
