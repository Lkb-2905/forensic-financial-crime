# PRD - Forensic & Financial Crime

## Vision
Accelerer les enquêtes financieres via un pipeline d'analyse reproductible.

## Probleme
Les investigations sont longues et manuelles, avec peu d'outils unifies.

## Utilisateurs
- Analystes fraude / Forensic
- Cabinets d'audit et conseil

## MVP (fonctionnalites)
- Scoring AML basique
- Recherche de preuves (CSV)
- Graphe de relations simple
- Audit d'acces
- Rapport HTML

## Evolutions
- Visualisation reseaux (graph)
- Export PDF/annexes legales
- Scoring multi-sources

## KPI
- Temps moyen d'enquete
- Nombre de cas detectes
- Qualite des preuves (completude)

## Entrees / Sorties
- Entrees: CSV/JSON d'exemple
- Sorties: `aml_report.csv`, `forensic_report.html`

## Contraintes
- Donnees anonymisees pour demo
- Demos rapides (CLI)

## Hors perimetre
- Integrations bancaires reelles
