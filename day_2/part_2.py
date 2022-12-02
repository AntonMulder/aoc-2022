from utils.io import readlines


def run(puzzle_input):
    scores = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    outcomes = (game.rstrip() for game in puzzle_input)
    return sum(scores[outcome] for outcome in outcomes)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
