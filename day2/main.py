bonus = {
    'X': 1,  # rock
    'Y': 2,  # paper
    'Z': 3  # scissors
}

points = {
    'win': 6,
    'draw': 3,
    'loose': 0
}

guide = {
    'A': {'Z': 'loose', 'Y': 'win', 'X': 'draw'},
    'B': {'X': 'loose', 'Z': 'win', 'Y': 'draw'},
    'C': {'Y': 'loose', 'X': 'win', 'Z': 'draw'}
}

cheat_sheet = {
    'X': 'loose',
    'Z': 'win',
    'Y': 'draw'
}


def open_game(file):
    with open(file) as f:
        lines = f.read().splitlines()
        print([line.split() for line in lines])
        return [line.split() for line in lines]


def calculate_score(games):
    scores = []
    for game in games:
        outcome = guide[game[0]].get(game[1])
        score = points.get(outcome) + bonus.get(game[1])
        scores.append(score)
    return sum(scores)


def calculate_best_move(games):
    scores = []
    for game in games:
        best_outcome = cheat_sheet.get(game[1])
        best_move = [key for key, value in guide[game[0]].items() if value == best_outcome][0]
        score = points.get(best_outcome) + bonus.get(best_move)
        scores.append(score)
    return sum(scores)


if __name__ == "__main__":
    games = open_game('test.txt')
    print(calculate_score(games))
    print(calculate_best_move(games))
