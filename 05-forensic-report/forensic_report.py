import argparse
import json
from datetime import datetime, timezone


def main() -> None:
    parser = argparse.ArgumentParser(description="Rapport forensic simple (HTML)")
    parser.add_argument("--input", default="observations.sample.json")
    parser.add_argument("--output", default="forensic_report.html")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as handle:
        items = json.load(handle)

    blocks = []
    for item in items:
        blocks.append(
            f"<div><strong>{item['severity']}</strong> - {item['title']}<br>{item['detail']}</div>"
        )
    html = f"""
    <html><head><meta charset="utf-8"></head><body>
    <h1>Rapport Forensic</h1>
    <p>Date: {datetime.now(timezone.utc).date()}</p>
    {''.join(blocks)}
    </body></html>
    """
    with open(args.output, "w", encoding="utf-8") as handle:
        handle.write(html.strip())
    print(f"Rapport genere: {args.output}")


if __name__ == "__main__":
    main()
