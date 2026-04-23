# app.py

import streamlit as st
from data_loader import load_data
from market_scanner import analyze_single_market
 
def main():
    st.title("Dashboard Quant")
    
    tab_scanner, tab_strategies, tab_backtest, tab_compare = st.tabs(
        ["Scanner de marchés", "Stratégies", "Backtest", "Comparaison"]
    )

    with tab_scanner:
        st.subheader("Scanner de marchés")

        # 1) Choix des tickers
        default_tickers = ["AAPL", "MSFT", "TSLA", "NVDA", "BTC-USD"]
        tickers_input = st.text_input(
            "Liste des tickers (séparés par des virgules)",
            value=",".join(default_tickers)
        )
        tickers = [t.strip() for t in tickers_input.split(",") if t.strip()]

        # 2) Choix de la date de fin (scan)
        scan_date = st.date_input("Date du scan (date de fin)", value=None)

        # 3) Bouton pour lancer le scan
        if st.button("Scanner"): # Ce bloc ne s’exécute que quand tu cliques sur le bouton.
            results = [] #  On va stocker les signaux (un dict par ticker).
            data_cache = {}

            for ticker in tickers:
                st.write(f"Chargement de {ticker}...")

                if scan_date:
                    df = load_data(ticker, start="2010-01-01", end=str(scan_date))
                else:
                    df = load_data(ticker, start="2010-01-01")

                # On garde le df pour les graphiques
                data_cache[ticker] = df

                # On calcule les régimes
                signal = analyze_single_market(df)
                signal["ticker"] = ticker # Nouvelle colonne créée. On ajoute le nom du ticker dans le dict.
                results.append(signal) # On ajoute ce dict à la liste des résultats.
                # À la fin de la boucle, results est une liste de signaux, un par ticker.


            # Affichage des résultats dans un tableau
            if results: # Si la liste n’est pas vide
                import pandas as pd
                df_results = pd.DataFrame(results)
                st.subheader("Résultats du scanner")
                st.dataframe(df_results)

                # Choix d'un ticker à visualiser
                selected_ticker = st.selectbox(
                    "Choisir un ticker à visualiser",
                    options=[r["ticker"] for r in results]
                )

                if selected_ticker:
                    df_sel = data_cache[selected_ticker]
                    st.subheader(f"Graphique : {selected_ticker}")
                    st.line_chart(df_sel["Close"])


        





    with tab_strategies:
        st.subheader("Strategies")
        st.write("à implémenter plus tard")

    with tab_backtest:
        st.subheader("Backtest")
        st.write("à implémenter plus tard")

    with tab_compare:
        st.subheader("Comparaison de stratégies")
        st.write("à implémenter plus tard.")

if __name__ == "__main__":
    main()
