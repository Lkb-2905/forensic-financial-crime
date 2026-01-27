import argparse
import csv
from collections import defaultdict


def score_transactions(rows):
    scores = []
    by_account = defaultdict(list)
    for row in rows:
        by_account[row["account"]].append(row)

    for row in rows:
        score = 0
        reasons = []
        amount = float(row["amount"])
        if amount >= 10000:
            score += 3
            reasons.append("montant_eleve")

        account_rows = by_account[row["account"]]
        same_day = [r for r in account_rows if r["date"] == row["date"]]
        if len(same_day) >= 2:
            score += 2
            reasons.append("fractionnement")

        if row["country"] not in ["FR", "EU"]:
            score += 2
            reasons.append("pays_risque")

        scores.append({**row, "score": score, "reasons": ",".join(reasons)})
    return scores


def main() -> None:
    parser = argparse.ArgumentParser(description="Scoring AML simple")
    parser.add_argument("--input", default="transactions.sample.csv")
    parser.add_argument("--output", default="aml_report.csv")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))

    scored = score_transactions(rows)
    with open(args.output, "w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=scored[0].keys())
        writer.writeheader()
        writer.writerows(scored)
    print(f"Rapport genere: {args.output}")


if __name__ == "__main__":
    main()
