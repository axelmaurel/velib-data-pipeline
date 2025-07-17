import requests
import json
import os

# === CONFIGURATION ===
API_KEY = "74dd96e189aecd0fec84dfea6dbe2e29d233611c"
CONTRACT_NAME = "Paris"
BASE_URL = "https://api.jcdecaux.com/vls/v1/stations"

# === Création dossier data si besoin ===
#os.makedirs("data", exist_ok=True)

# === Requête à l’API ===
params = {
    "apiKey": API_KEY
    #"contract": CONTRACT_NAME
}
response = requests.get(BASE_URL, params=params)

print("URL appelée :", response.url)


# === Vérification et sauvegarde ===
if response.status_code == 200:
    stations_data = response.json()
    
    with open("data/raw_stations.json", "w", encoding="utf-8") as f:
        json.dump(stations_data, f, indent=2, ensure_ascii=False)
    
    print(f"{len(stations_data)} stations récupérées et sauvegardées.")
else:
    print("Erreur lors de l'appel API :", response.status_code)
