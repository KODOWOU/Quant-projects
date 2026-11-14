# Scanner de Marchés & Framework Quantitatif — Documentation Technique

## Objectif

Ce document décrit l’architecture technique, les choix méthodologiques et le fonctionnement interne du framework de scan de marchés et de stratégies quantitatives.

L’objectif est de détailler comment les données sont traitées, comment les régimes de marché sont détectés et comment les décisions d’investissement sont générées.

## NB: pour visualiser les résultats de compilaion du code, veuillez ouvrir le notebook exploration.ipynb

---

## Architecture du système

Le framework suit une pipeline modulaire :

```id="g7k1pw"
Données → Détection des régimes → Scanner → Sélection de stratégie → Backtest → Visualisation
```

Chaque module est indépendant et extensible.

---

## Structure du projet

```id="zfdjbt"
Trading strategies backtest/
│
├── data_loader.py          # Chargement des données (Yahoo Finance, nettoyage)
├── regimes.py              # Détection des régimes de marché (trend, vol, range, impulse)
├── market_scanner.py       # Scanner multi-actifs + génération de signaux
├── indicator_lib.py        # Indicateurs techniques (RSI, VWAP, etc.)
│
├── strategies/
│   ├── ema_cross.py        # Stratégie de croisement de moyennes mobiles
│   ├── ichimoku.py         # Stratégie Ichimoku
│   ├── rsi_strategies.py   # Stratégies basées sur RSI
│
├── backtest_py/
│   ├── backtest.py         # Engine de backtesting principal
│   ├── metrics.py          # Métriques de performance (Sharpe, drawdown, etc.)
│
├── app.py                  # Dashboard Streamlit
├── main.py                 # Script principal / tests
├── exploration.ipynb       # Notebook d’exploration et prototypage
```

---

## Couche Données

### Source

* Yahoo Finance via `yfinance`

### Fonctionnalités

* Système de retry automatique
* Vérification des données OHLCV
* Correction des structures MultiIndex
* Nettoyage de l’index temporel
* Gestion des valeurs manquantes

### Sortie

DataFrame propre et exploitable indexé par date.

---

## Détection des régimes de marché

Le système identifie 4 dimensions indépendantes du marché.

---

### 1. Régime de volatilité

**Méthode :**

* ATR (Average True Range)
* Volatilité relative

**Classes :**

* Faible volatilité
* Volatilité normale
* Forte volatilité

---

### 2. Régime de tendance

**Méthode :**

* Pente d’une moyenne mobile
* Seuils dynamiques

**Classes :**

* Tendance haussière
* Tendance baissière
* Neutre
* Début de tendance

---

### 3. Détection de range

**Méthode :**

* Bollinger Bandwidth
* Contraction de volatilité

**Logique :**
Bandes étroites + faible volatilité → marché en range

---

### 4. Détection d’impulsion

**Méthode :**

* Rate of Change (ROC)
* Breakout sur n périodes
* Spike de volume

**Classes :**

* Impulsion haussière
* Impulsion baissière

---

## Scanner de marchés

Le scanner agrège les signaux sur plusieurs actifs.

### Entrées

* Liste de tickers
* Date d’analyse

### Sorties

Pour chaque actif :

* Régime de volatilité
* Tendance
* Détection de range
* Signal d’impulsion
* Début de tendance

### Exemples de sorties

* « marché calme en range »
* « début de tendance haussière »
* « breakout haussier »
* « tendance baissière »

---

## Logique de sélection des stratégies

Les stratégies sont associées aux régimes de marché :

| Stratégie      | Régime optimal            |
| -------------- | ------------------------- |
| Mean Reversion | Range + faible volatilité |
| EMA Cross      | Début de tendance         |
| Breakout       | Impulsion                 |
| Ichimoku       | Tendance établie          |

Cette approche permet une allocation dynamique.

---

## Moteur de backtest (en cours)

### Fonctionnalités prévues

* Long-only et long/short
* Position sizing basé sur ATR
* Stop-loss / take-profit
* Extraction des trades
* Courbe d’equity

### Métriques

* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown
* CAGR
* Win rate

---

## Module de comparaison (en cours)

* Backtests multiples
* Comparaison des performances
* Superposition des equity curves
* Classement des stratégies

---

## Couche de visualisation

Dashboard développé avec Streamlit.

### Modules

1. Scanner de marchés

   * Analyse multi-actifs
   * Tableau des signaux
   * Graphiques de prix

2. Stratégies

   * Description
   * Paramètres

3. Backtest

   * Résultats
   * Performances

4. Comparaison

   * Analyse comparative

---

## Principes de conception

### Modularité

Chaque composant est indépendant.

### Extensibilité

Ajout facile de nouvelles stratégies ou modèles.

### Reproductibilité

Pipeline déterministe.

### Interprétabilité

Les signaux sont lisibles et compréhensibles.

---

## Intuition économique

Le framework repose sur plusieurs principes clés :

* Les marchés évoluent selon différents régimes
* Aucune stratégie ne fonctionne en permanence
* Les systèmes adaptatifs sont plus robustes

---

## Known issues / Rebuild in progress

> The backtest part of this project will be merged into **Regime-Aware Allocation** (link will be added here). Known issues in the current version:

- **Look-ahead bias in Ichimoku:** `chikou = Close.shift(-26)` is used in the entry rule, so the strategy reads the price 26 days ahead. Ichimoku results must not be used.
- **Look-ahead bias in regime detection:** thresholds are quantiles computed on the full history (for example `hv.quantile(0.30)`), so a 2016 regime depends on 2025 data.
- **Position sizing:** the backtest trades one share on a 10,000 USD capital (exposure below 1%), so equity curves and Sharpe ratios are not meaningful.
- `scan_markets()` crashes (`last - 1` on a Timestamp).
- Not implemented yet: the VWAP mean-reversion strategy (only the VWAP indicator exists in `indicator_lib.py`), position sizing and backtest visualization. The three empty placeholder files were removed in November 2026.

---

## Limites

* Backtester encore en développement
* Seuils de régimes non optimisés

---

## Améliorations possibles

* Modèles de régimes avancés (HMM, clustering)
* Walk-forward optimization
* Intégration multi-actifs
* Risk parity / volatility targeting

---

## Auteur

Kodjo Anthelme Kodowou
Étudiant en M2 Ingénierie Financière de Marché (Université de Lorraine)

---

## Disclaimer

Ce projet est destiné à l’apprentissage et à la recherche.
Il ne constitue pas un conseil en investissement.
