import pandas as pd
import sqlite3

# Connexion
conn = sqlite3.connect("velib_data.db")

# Lecture des données brutes
df_bronze = pd.read_sql("SELECT * FROM stations_bronze", conn)
print(df_bronze.head())

# Copie pour Silver
df_silver = df_bronze.copy()

# Conversion du timestamp
df_silver["last_update"] = pd.to_datetime(df_silver["last_update"], unit="ms")

# Statut en majuscule
df_silver["status"] = df_silver["status"].str.upper()

# Supprimer doublons
df_silver.drop_duplicates(inplace=True)

print(df_silver.info())

df_silver.to_sql("stations_silver", conn, if_exists="replace", index=False)

df_gold = df_silver.copy()

# Ajout des colonnes
df_gold["pct_availability"] = (df_gold["available_bikes"] / df_gold["bike_stands"]) * 100 # pourcentage de disponibilité par station
df_gold["is_full"] = (df_gold["available_bike_stands"] == 0).astype(int)
df_gold["is_empty"] = (df_gold["available_bikes"] == 0).astype(int)

# Sauvegarde dans SQLite
df_gold.to_sql("stations_gold", conn, if_exists="replace", index=False)

print("Tables Silver et Gold créées avec succès !")
print(df_gold.head())
