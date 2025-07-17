import json
import sqlite3

# === Connexion à la base SQLite ===
conn = sqlite3.connect("velib_data.db")
cursor = conn.cursor()

# === Création de la table si elle n'existe pas ===
cursor.execute("""
CREATE TABLE IF NOT EXISTS stations_bronze (
    number INTEGER,
    contract_name TEXT,
    name TEXT,
    address TEXT,
    lat REAL,
    lng REAL,
    banking INTEGER,
    bonus INTEGER,
    bike_stands INTEGER,
    available_bike_stands INTEGER,
    available_bikes INTEGER,
    status TEXT,
    last_update INTEGER
)
""")

# === Chargement du fichier JSON ===
with open("data/raw_stations.json", "r", encoding="utf-8") as f:
    stations = json.load(f)

# === Insertion dans la table ===
for station in stations:
    cursor.execute("""
    INSERT INTO stations_bronze VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        station.get("number"), # Identifiant station
        station.get("contract_name"), # Nom du contrat (ville)
        station.get("name"), # Nom station
        station.get("address"), # Adresse
        station["position"]["lat"], # Latitude
        station["position"]["lng"], # Longitude
        int(station.get("banking", False)), # Paiement carte
        int(station.get("bonus", False)), # Bonus
        station.get("bike_stands"), # Capacité totale
        station.get("available_bike_stands"), # Bornes libres
        station.get("available_bikes"), # Vélos dispos
        station.get("status"), #Statut (OPEN/CLOSED)
        station.get("last_update") #Timestamp
    ))

# === Commit et fermeture ===
conn.commit()
conn.close()

print("Données insérées dans stations_bronze avec succès !")
