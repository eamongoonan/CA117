from sys import stdin

if (__name__ == "__main__"):
    times = {
        line.strip().split()[0]: line.strip().split()[1:]
        for line in stdin
        if all(map(lambda a: a.replace(":", "").isnumeric(), line.strip().split()[1:]))
    }

    time_to_sec = lambda t: int(t.split(":")[0]) * 60 + int(t.split(":")[1])
    festest = min(
        times.items(),
        key=lambda kv: time_to_sec(min(kv[1], key=time_to_sec))
    )

    print(festest[0], ":", min(festest[1], key=time_to_sec))
