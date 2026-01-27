import argparse
import csv
from datetime import datetime


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit acces et comptes inactifs")
    parser.add_argument("--input", default="accounts.sample.csv")
    parser.add_argument("--days", type=int, default=90)
    args = parser.parse_args()

    limit = datetime.now().date().toordinal() - args.days
    with open(args.input, "r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            last_login = datetime.strptime(row["last_login"], "%Y-%m-%d").date().toordinal()
            inactive = last_login < limit
            if inactive or row["role"] == "admin":
                print(row, "inactive" if inactive else "active")


if __name__ == "__main__":
    main()
