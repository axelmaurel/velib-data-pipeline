import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px
import os
from datetime import datetime

# === CONFIGURATION PAGE ===
st.set_page_config(page_title="Dashboard Vélib", layout="wide")

# === CONNEXION BDD ===
conn = sqlite3.connect("velib_data.db")

# === SIDEBAR ===
st.sidebar.header("📌 Menu")
if st.sidebar.button("🔄 Rafraîchir les données"):
    with st.spinner("Mise à jour en cours..."):
        os.system("python 01_ingest.py")
        os.system("python 02_load_sqlite.py")
        os.system("python 03_transform.py")
    st.sidebar.success("Mise à jour terminée ✅")

# Upload fichier JSON
uploaded_file = st.sidebar.file_uploader("Uploader un fichier JSON", type=["json"])
if uploaded_file:
    df_new = pd.read_json(uploaded_file)
    df_new.to_sql("stations_bronze", conn, if_exists="replace", index=False)
    st.sidebar.success("Fichier importé et inséré ✅")

# === CHARGER TABLE GOLD ===
df = pd.read_sql("SELECT * FROM stations_gold", conn)

# === FILTRES ===
st.sidebar.header("Filtres")
ville = st.sidebar.selectbox("Ville", options=["Toutes"] + sorted(df["contract_name"].unique().tolist()))
status = st.sidebar.multiselect("Statut", options=df["status"].unique(), default=df["status"].unique())

# Filtrage
df_filtered = df.copy()
if ville != "Toutes":
    df_filtered = df_filtered[df_filtered["contract_name"] == ville]
if status:
    df_filtered = df_filtered[df_filtered["status"].isin(status)]

# === KPIs ===
st.title("🚲 Dashboard Vélib")
col1, col2, col3 = st.columns(3)
col1.metric("Stations", len(df_filtered))
col2.metric("Disponibilité moyenne (%)", round(df_filtered["pct_availability"].mean(), 2))
col3.metric("Stations fermées", (df_filtered["status"] != "OPEN").sum())

# === DOWNLOAD BUTTON ===
st.download_button("📥 Télécharger données (CSV)", df_filtered.to_csv(index=False), "stations_filtered.csv", "text/csv")

# === TABS ===
tab1, tab2, tab3 = st.tabs(["Vue Globale", "Carte", "Analyse Ville"])

with tab1:
    st.subheader("Top 10 stations avec le plus de vélos")
    top10 = df_filtered.sort_values("available_bikes", ascending=False).head(10)
    fig1 = px.bar(top10, x="name", y="available_bikes", title="Top 10 stations")
    st.plotly_chart(fig1, use_container_width=True)

with tab2:
    st.subheader("Carte des stations")
    fig2 = px.scatter_mapbox(df_filtered,
                             lat="lat", lon="lng",
                             color="pct_availability",
                             size="bike_stands",
                             hover_name="name",
                             mapbox_style="open-street-map",
                             zoom=11)
    st.plotly_chart(fig2, use_container_width=True)

with tab3:
    st.subheader("Disponibilité moyenne par ville")
    dispo_par_ville = df.groupby("contract_name")["pct_availability"].mean().reset_index()
    fig3 = px.bar(dispo_par_ville, x="contract_name", y="pct_availability", title="Disponibilité par ville")
    st.plotly_chart(fig3, use_container_width=True)

conn.close()
