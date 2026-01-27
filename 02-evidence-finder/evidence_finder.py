import argparse
import csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Evidence Finder CSV")
    parser.add_argument("--input", default="evidence.sample.csv")
    parser.add_argument("--keyword", required=True)
    args = parser.parse_args()

    matches = []
    with open(args.input, "r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if args.keyword.lower() in row["description"].lower():
                matches.append(row)

    for row in matches:
        print(row)
    print(f"Total: {len(matches)}")


if __name__ == "__main__":
    main()
