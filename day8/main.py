def count_trees(file):
    with open(file, "r") as f:
        trees = f.read().splitlines()
    print(trees)
    count_center(trees)
    return count_edges(trees)


def count_edges(trees):
    top_and_bottom = len(trees[0])*2
    edges = (len(trees)*2)-4
    return edges + top_and_bottom

def count_center(trees):
    # center = [row[1:-1] for row in trees[1:-1]]
    for row in trees[1:-1]:
        print(row)


if __name__ == "__main__":
    print(count_trees('test.txt'))
