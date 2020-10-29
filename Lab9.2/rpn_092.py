from math import sqrt

def calculator(expression):
    vals = expression.split()
    ops = []
    while not vals[-1].isnumeric():
        ops.append(vals.pop())
    vals = [float(v) for v in vals]

    while 1 < len(vals) or ops:
        {
            "+": lambda l: l.append(l.pop() + l.pop()),
            "-": lambda l: l.append(-l.pop() + l.pop()),
            "*": lambda l: l.append(l.pop() * l.pop()),
            "/": lambda l: l.append((1 / l.pop()) * l.pop()),
            "n": lambda l: l.append(-l.pop()),
            "r": lambda l: l.append(sqrt(l.pop()))
        }[ops.pop()](vals)

    return vals.pop()
