import string

contents = list(string.ascii_lowercase) + list(string.ascii_uppercase)
priority_guide = dict(zip(contents, list(range(1, 53))))


def open_rucksacks(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
        return lines


def split_compartments(compartments):
    no_items = int(len(compartments)/2)
    comp_1 = compartments[:no_items]
    comp_2 = compartments[no_items:]
    return comp_1, comp_2


def locate_items(compartment_1, compartment_2):
    item = set(compartment_1).intersection(set(compartment_2))
    return list(item)[0]


def get_priorities(rucksacks):
    priorities = []
    for compartments in rucksacks:
        comp_1, comp_2 = split_compartments(compartments)
        item = locate_items(comp_1, comp_2)
        priority = priority_guide.get(item)
        priorities.append(priority)
    return priorities


def find_badge_priorities(rucksacks):
    priorities = []
    for i in range(0, len(rucksacks), 3):
        badge = set.intersection(set(rucksacks[i]), set(rucksacks[i+1]), set(rucksacks[i+2]))
        badge = list(badge)[0]
        priority = priority_guide.get(badge)
        priorities.append(priority)
    return priorities


if __name__ == "__main__":
    rucksacks = open_rucksacks('input.txt')
    print(sum(get_priorities(rucksacks)))
    print(sum(find_badge_priorities(rucksacks)))