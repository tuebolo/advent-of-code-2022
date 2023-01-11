def load(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
    return lines


if __name__ == "__main__":
    data = load('test.txt')
    print(data)
