def build_dictionary(file_name):
    with open(file_name) as file:
        return {
            line.strip().split()[0]: int(line.strip().split()[1])
            for line in file
        }

def extract_range(dicc, low, high):
    return {
        k: v for k, v in dicc.items()
        if low <= v and v <= high
    }
