📘 Scanner de Marchés & Framework Quantitatif de Stratégies et Backtests
🎯 Vue d’ensemble
Ce projet implémente un framework quantitatif complet permettant :

d’identifier automatiquement les régimes de marché (tendance, range, impulsion, volatilité)

de scanner plusieurs actifs pour détecter des opportunités

de sélectionner une stratégie adaptée au régime détecté

de backtester ces stratégies sur une période future

de comparer plusieurs stratégies dans un environnement interactif

L’objectif est de construire un outil réaliste, modulaire et pédagogique, similaire aux environnements utilisés dans les desks quantitatifs (CTA, systematic macro, equity quant).

⭐ Fonctionnalités principales
Téléchargement robuste des données (Yahoo Finance)

Détection de 4 régimes de marché :

Volatilité (low/normal/high)

Tendance (uptrend/downtrend/neutral)

Range (marché plat)

Impulsion (explosion haussière/baissière)

Scanner multi‑actifs

Analyse d’un marché à une date donnée (scan historique)

Sélection de stratégie basée sur le régime

Backtesting modulaire (en développement)

Comparaison de stratégies (en développement)

Dashboard Streamlit multi‑onglets

Architecture pédagogique et extensible

📁 Structure du projet
Code
quant-market-scanner/
│
├── data_loader.py          # Téléchargement robuste des données OHLCV
├── regimes.py              # Détection des régimes de marché
├── market_scanner.py       # Analyse d’un marché + scanner multi-actifs
│
├── strategies/             # (À compléter)
│   ├── ema_cross.py
│   ├── ichimoku.py
│   ├── breakout.py
│   └── mean_reversion.py
│
├── backtester/             # (À compléter)
│   ├── engine.py
│   ├── metrics.py
│   └── utils.py
│
├── app.py                  # Dashboard Streamlit
├── main.py                 # Script de test local
└── README.md
🧠 Méthodologie
1. Chargement des données
Données OHLCV téléchargées via yfinance

Système de retry automatique en cas d’erreur réseau

Correction des MultiIndex Yahoo Finance

Vérification stricte des colonnes obligatoires

Index temporel propre et nettoyé

2. Détection des régimes de marché
Le framework identifie quatre régimes fondamentaux :

🔹 Volatility Regime
Classe le marché en :

low_vol

normal

high_vol

Basé sur ATR et volatilité relative.

🔹 Trend Regime
Détecte :

uptrend

downtrend

neutral

début de tendance (transition neutral → trend)

Basé sur la pente d’une moyenne mobile et des seuils dynamiques.

🔹 Range Regime
Détecte les marchés plats via :

Bollinger Bandwidth

contraction de volatilité (ATR ratio)

🔹 Impulse Regime
Détecte les explosions de prix via :

ROC (Rate of Change)

breakout de n jours

volume spike

3. Scanner de marchés
Le scanner analyse plusieurs actifs simultanément et renvoie :

Volatilité actuelle

Tendance

Range ou non

Impulsion

Début de tendance

Résumé intelligent

Exemples de signaux :

“marché calme en range”

“début de tendance haussière”

“marché explosif haussier”

“tendance baissière”

4. Sélection de stratégie (basée sur le régime)
Stratégie	Régime optimal
Mean Reversion	Range + Low Vol
EMA Cross	Début de tendance
Breakout	Impulsion
Ichimoku	Tendance établie

Le dashboard permettra de choisir une stratégie en fonction du régime détecté.

5. Backtesting (en développement)
Le moteur de backtest supportera :

Positions long-only ou long/short

Position sizing basé sur ATR

Stop-loss / take-profit

Extraction des trades

Equity curve

Métriques de performance :

Sharpe

Sortino

Max drawdown

CAGR

Win rate

6. Comparaison de stratégies (en développement)
Le module permettra :

Backtests multiples

Comparaison des métriques

Superposition des equity curves

Classement des stratégies

7. Dashboard Streamlit
Le dashboard est organisé en quatre onglets :

🟦 1. Scanner de marchés
Saisie des tickers

Choix de la date du scan

Analyse multi‑actifs

Tableau des signaux

Graphique du prix

🟩 2. Stratégies
Liste des stratégies

Description

Paramètres ajustables

🟧 3. Backtest
Choix de la stratégie

Choix de la période

Résultats du backtest

🟥 4. Comparaison
Sélection de plusieurs stratégies

Comparaison des performances

📊 Intuition économique
Régimes de marché
Les marchés changent de comportement selon la volatilité, la tendance et la structure.
Un système robuste doit s’adapter à ces régimes.

Trend Following
Les tendances persistent souvent à cause des flux macro et institutionnels.

Mean Reversion
Les marchés en range oscillent autour d’un équilibre.

Breakout / Impulse
Les explosions de prix suivent souvent des phases de contraction.

Approche dynamique
Un système statique échoue dans un marché dynamique.
Un système basé sur les régimes s’adapte automatiquement.

📈 Résultats attendus
Détection précise des débuts de tendance

Identification des zones de contraction de volatilité

Détection des breakouts

Stratégies plus robustes qu’un modèle unique

Meilleure adaptation aux conditions de marché

⚠ Limites
Pas encore de coûts de transaction

Pas de slippage

Données Yahoo Finance parfois incomplètes

Backtester en cours de développement

Seuils de régimes à optimiser

🚀 Améliorations possibles
Ajout de risk parity / volatility targeting

Modèles de régimes avancés (HMM, clustering)

Backtests multi‑actifs

Walk‑forward optimization

Intégration d’Ollama pour :

commentaires automatiques

rapports de marché

explication pédagogique des signaux

🛠 Technologies utilisées
Python

Pandas, NumPy

yfinance

Streamlit

Matplotlib / Plotly

Architecture modulaire orientée objet

👤 Auteur
Kodjo Anthelme Kodowou  
Analyste Quantitatif Junior
Nancy, France

📜 Disclaimer
Ce projet est destiné à l’apprentissage et à la recherche.
Il ne constitue en aucun cas un conseil en investissement.
