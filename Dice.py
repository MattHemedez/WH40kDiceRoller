import random
from collections import defaultdict

class Dice:
    def __init__(self):
        pass

    @staticmethod
    def roll(numSides):
        return random.randint(1, numSides)


if __name__ == "__main__":
    diceResults = defaultdict(int)
    sum = 0
    for i in range(10000):
        sum += 1
        diceResults[Dice.roll(6)] += 1
    for diceRoll, num in diceResults.items():
        print("Roll:", diceRoll, "\n\tNumber of times rolled:", num)
        print("\tNumber of times rolled:", num)
        print("\tPercentage of times rolled:", num/sum)
