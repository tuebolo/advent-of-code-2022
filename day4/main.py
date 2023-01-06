def open_assignments(file):
    with open(file, "r") as f:
        assignments = [line.split(',') for line in f.read().splitlines()]
        assignments = [convert_to_range(section) for sections in assignments for section in sections]
        return assignments


def convert_to_range(section):
    a, b = section.split('-')
    a, b, = int(a), int(b)
    return set(range(a, b + 1))


def check_fully_overlap(assignments):
    overlap_count = 0
    for i in range(0, len(assignments), 2):
        if assignments[i].issubset(assignments[i + 1]):
            overlap_count += 1
        elif assignments[i + 1].issubset(assignments[i]):
            overlap_count += 1
    return overlap_count


def check_overlap(assignments):
    overlap_count = 0
    for i in range(0, len(assignments), 2):
        if set.intersection(set(assignments[i]), set(assignments[i+1])):
            overlap_count += 1
    return overlap_count


if __name__ == "__main__":
    assignments = open_assignments('input.txt')
    print(check_fully_overlap(assignments))
    print(check_overlap(assignments))

