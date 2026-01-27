import argparse
import csv
from collections import Counter


def main() -> None:
    parser = argparse.ArgumentParser(description="Graph de relations (simple)")
    parser.add_argument("--input", default="relations.sample.csv")
    args = parser.parse_args()

    counter = Counter()
    with open(args.input, "r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            counter[row["source"]] += 1
            counter[row["target"]] += 1

    for node, degree in counter.most_common():
        print(f"{node}: {degree}")


if __name__ == "__main__":
    main()
