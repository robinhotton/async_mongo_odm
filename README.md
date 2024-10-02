# FastAPI MongoDB Project

## Description

Ce projet est une application web construite avec **FastAPI** pour le backend et **MongoDB** pour le stockage des données. L'application utilise **Pydantic** pour la validation des données et des schémas de réponse, et gère le cycle de vie de l'application avec les nouveaux gestionnaires d'événements de FastAPI.

## Prérequis

- Python 3.8 ou version ultérieure
- MongoDB (local ou distant)
- `pip` pour l'installation des dépendances

## Structure du Projet

```bash
async_mongo_odm/
│
├── app/                    # Code source de l'application
│   ├── main.py             # Point d'entrée de l'application & configure FastAPI
│   ├── config.py           # Configuration de l'application, dont la connexion à MongoDB
│   ├── models/             # Modèles Beanie pour MongoDB (ODM)
│   ├── routers/            # Endpoints de l'application
│   ├── schemas/            # Schémas de validation des données avec Pydantic
│   └── services/           # Logique métier reliant modèles et routeurs
│
├── .env                    # Variables d'environnement pour la configuration
├── .env.example            # Template d'exemple pour les variables d'environnement
├── .venv/                  # Environnement virtuel Python
├── .gitignore              # Fichiers et dossiers à ignorer par Git
├── README.md               # Documentation du projet
├── requirements.txt        # Dépendances du projet
└── run.py                  # Script pour lancer l'API
```

## Installation & Configuration

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/robinhotton/async_mongo_odm.git
   cd async_mongo_odm
   ```

2. **Créer un fichier `.env`**

   Créez un fichier `.env` à la racine du projet et configurez les variables suivant le .env.example :

   Adaptez les informations en fonction de la configuration de votre base de données MongoDB Atlas.

   - username : Le nom de l'utilisateur Atlas
   - password : Le mot de passe de l'utilisateur Atlas
   - cluster : Le cluster du projet Atlas
   - database : Le nom de la base de données
   - secret_key : La clé d'encodage
   - algorithm : L'algorithm pour encoder les password

   Si vous souhaitez lancer en localhost, supprimez les champs username, password et cluster.

## Utilisation

1. **Démarrer l'application**

   Pour lancer l'application, utilisez la commande suivante :

   ```bash
   python run.py
   ```

   Cela configurera l'environnement et démarrera le serveur de développement FastAPI avec rechargement automatique.

2. **Accéder à l'application**

   Ouvrez votre navigateur et accédez à [`http://127.0.0.1:8000`](http://127.0.0.1:8000). Vous verrez la page de documentation interactive générée automatiquement par FastAPI.

   Vous pouvez également accéder à la documentation interactive via [`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) ou à la documentation alternative via [`http://127.0.0.1:8000/redoc`](http://127.0.0.1:8000/redoc).
