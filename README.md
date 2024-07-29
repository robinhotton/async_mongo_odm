# FastAPI MongoDB Project

## Description

Ce projet est une application web construite avec **FastAPI** pour le backend et **MongoDB** pour le stockage des données. L'application utilise **Pydantic** pour la validation des données et des schémas de réponse, et gère le cycle de vie de l'application avec les nouveaux gestionnaires d'événements de FastAPI.

## Prérequis

- Python 3.8 ou version ultérieure
- MongoDB (local ou distant)
- `pip` pour l'installation des dépendances

## Installation

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/robinhotton/async_mongo_odm.git
   cd async_mongo_odm
   ```

2. **Créer un environnement virtuel**

   ```bash
   python -m venv .venv
   ```

3. **Activer l'environnement virtuel**

   - **Windows**

     ```bash
     .venv\Scripts\activate
     ```

   - **macOS/Linux**

     ```bash
     source .venv/bin/activate
     ```

4. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Créer un fichier `.env`**

   Créez un fichier `.env` à la racine du projet et configurez les variables suivantes :

   ```bash
   MONGODB_URL=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/
   DATABASE_NAME=<database>
   ```

   Adaptez l'URL en fonction de la configuration de votre base de données MongoDB.

   - username : Le nom de l'utilisateur Atlas
   - password : Le mot de passe de l'utilisateur Atlas
   - cluster : Le cluster du projet Atlas
   - database : Le nom de la base de données

   Par défaut, le projet ce lance sur le **localhost** sur la base de données **myDatabase** : `mongodb://localhost:27017/myDatabase`

## Structure du Projet

```bash
async_mongo_odm/
│
├── .venv/                  # Environnement virtuel
├── app/                    # Code source de l'application
│   ├── main.py             # Point d'entrée de l'application
│   ├── config.py           # Configuration de l'application
│   ├── models/             # Modèles Pydantic pour la validation
│   ├── routers/            # Routes de l'application
│   ├── schemas/            # Schémas de données (Pydantic)
│   └── services/           # Services et logique métier
│
├── .env                    # Variables d'environnement
├── .gitignore              # Fichiers et dossiers à ignorer par Git
├── README.md               # Première de couverture du projet
└── requirements.txt        # Dépendances du projet
```

## Utilisation

1. **Démarrer l'application**

   Pour lancer l'application, utilisez la commande suivante :

   ```bash
   uvicorn app.main:app --reload
   ```

   Cela démarre le serveur de développement FastAPI avec rechargement automatique.

2. **Accéder à l'application**

   Ouvrez votre navigateur et accédez à [`http://127.0.0.1:8000`](http://127.0.0.1:8000). Vous verrez la page de documentation interactive générée automatiquement par FastAPI.

   Vous pouvez également accéder à la documentation interactive via [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) ou à la documentation alternative via [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc).
