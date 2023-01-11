def load_steps(file):
    with open(file, "r") as f:
        lines = f.read().splitlines()
        return [(line.split()[0], int(line.split()[1])) for line in lines]


def make_moves(moves):
    for move, step in moves:
        if move == 'R':
            pass

if __name__ == "__main__":
    moves = load_steps('test.txt')
    make_moves(moves)