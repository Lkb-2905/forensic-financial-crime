# Forensic & Financial Crime (demo portfolio)

Objectif: couvrir un mini-pipeline forensic avec des modules simples
et des sorties faciles a demonstrer.

## Contenu
- `01-transaction-investigation`: scoring AML basique.
- `02-evidence-finder`: recherche de preuves dans CSV.
- `03-entity-graph`: centralite simple sur relations.
- `04-access-audit`: comptes inactifs et acces admin.
- `05-forensic-report`: rapport HTML a partir d'observations.

## Demarrage rapide (demos)
```
cd 01-transaction-investigation
python aml_scoring.py --input transactions.sample.csv --output aml_report.csv

cd ../02-evidence-finder
python evidence_finder.py --input evidence.sample.csv --keyword suspect

cd ../03-entity-graph
python entity_graph.py --input relations.sample.csv

cd ../04-access-audit
python access_audit.py --input accounts.sample.csv --days 90

cd ../05-forensic-report
python forensic_report.py --input observations.sample.json --output forensic_report.html
```

## Captures conseillees
- `01-transaction-investigation/aml_report.csv`
- Terminal: evidence finder + entity graph + access audit.
- `05-forensic-report/forensic_report.html`

## Dependances
Voir `requirements.txt`.

## Roadmap et suggestions
- `ROADMAP.md`
- `CODE_SUGGESTIONS.md`
