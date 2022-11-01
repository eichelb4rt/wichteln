from operator import itemgetter
import random
import argparse
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser(description="Jeder bekommt irgendwie random ein Geschenk. Gebt beim Einsammeln der Geschenke jeder Person eine Nummer. Diese Nummer klebt ihr an die Person und an das Geschenk. Man fängt bei 0 an zu zählen.")
    parser.add_argument("n", type=int, help="Anzahl der Wichtler")
    args = parser.parse_args()
    players = list(range(args.n))
    random.shuffle(players)
    presents = [[player, players[(i + 1) % len(players)]] for i, player in enumerate(players)]
    presents.sort(key=itemgetter(0))
    print(tabulate(presents, headers=["Person", "bekommt Geschenk"], tablefmt="rounded_grid", colalign=("right", "left")))


if __name__ == "__main__":
    main()
