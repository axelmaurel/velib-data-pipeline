# 🚲 Dashboard Vélib avec Streamlit et SQLite

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-red)](https://streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Description
Ce projet montre comment construire un **pipeline complet** pour analyser les stations Vélib via l'API JCDecaux :
- **Ingestion** des données depuis l'API
- **Stockage** dans SQLite (Bronze → Silver → Gold)
- **Visualisation** interactive avec Streamlit

---

## ✅ Objectif & Utilité du projet
Vélib’ est un service de vélos en libre-service disponible à Paris et dans certaines villes d’Île-de-France. Les données sont accessibles via l’API JCDecaux et incluent :  
- Nom et adresse des stations  
- Nombre de vélos disponibles  
- Nombre de places libres  
- Coordonnées GPS  
- Statut (OPEN/CLOSED)  

### **Objectif :**
Construire un pipeline de données complet pour analyser la disponibilité des vélos en temps réel, en appliquant les bonnes pratiques d’ingestion, de transformation et de visualisation.

### **Étapes :**
- **Ingestion** des données depuis l’API
- **Transformation** avec le modèle **Bronze → Silver → Gold**
- **Enrichissement** avec des KPIs :
  - Taux de disponibilité
  - Stations pleines ou vides
- **Stockage** dans **SQLite**
- **Visualisation interactive** avec Streamlit

### **Utilité :**
- Pour un **gestionnaire de flotte** : optimiser la répartition des vélos
- Pour un **citoyen** : trouver rapidement un vélo ou une place disponible
- Pour un **analyste data** : explorer la demande et anticiper les besoins

---

## ✅ Fonctionnalités
✔ Rafraîchissement des données en un clic  
✔ Téléchargement CSV des données filtrées  
✔ Upload d'un fichier JSON externe  
✔ Carte interactive avec disponibilité des stations  
✔ KPIs et graphiques dynamiques  

---

## 📂 Structure du projet
velib_data_project/
├── 01_ingest.py # Ingestion depuis l'API
├── 02_load_sqlite.py # Stockage dans SQLite
├── 03_transform.py # Nettoyage et enrichissement
├── 04_visualisation.py # Dashboard Streamlit
├── run_pipeline.bat # Script pour automatiser la pipeline
├── requirements.txt
├── README.md
├── .gitignore
├── diagram.png # Schéma du pipeline

---

## ⚙️ Installation
1. Clonez le projet :
   ```bash
   git clone https://github.com/<TON_USER>/velib_data_project.git
   cd velib_data_project

2. Créez un environnement virtuel et installez les dépendances :
    pip install -r requirements.txt


---

## ▶️ Execution
1. Lancer le pipeline complet :
    python 01_ingest.py
    python 02_load_sqlite.py
    python 03_transform.py

2. Lancer le dashboard Streamlit :
    streamlit run 04_visualisation.py

---

## ▶️ Aperçu
![Vue globle](image.png)
![Carte](image-1.png)
![Analyse ville](image-2.png)

## ✅ Tech Stack
- Python (requests, pandas, Streamlit, Plotly)
- SQLite
- API JCDecaux Vélib

## 🔗 Auteur
Projet réalisé par Axel Maurel Angu à l'aide de ChatGPT

## ✅ Diagramme Pipeline (style moderne)
![velib_pipeline_diagram](velib_pipeline_diagram-1.png)
