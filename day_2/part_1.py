from utils.io import readlines


def run(puzzle_input):
    scores = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    outcomes = (game.rstrip() for game in puzzle_input)
    return sum(scores[outcome] for outcome in outcomes)


if __name__ == "__main__":
    print(run(readlines("data/puzzle_input.txt")))
