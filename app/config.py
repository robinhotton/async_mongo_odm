import os
from dotenv import load_dotenv
from urllib.parse import quote_plus


def get_mongodb_uri():
    """Construit l'URI de connexion MongoDB et le retourne, ou retourne localhost si les informations sont manquantes."""
    USERNAME = os.getenv("USERNAME")
    PASSWORD = os.getenv("PASSWORD")
    CLUSTER = os.getenv("CLUSTER")

    # Encodage des informations d'identification
    encoded_username = quote_plus(USERNAME) if USERNAME else ''
    encoded_password = quote_plus(PASSWORD) if PASSWORD else ''

    # Construction de l'URI de connexion
    mongodb_uri = (
        f"mongodb+srv://{encoded_username}:{encoded_password}@{CLUSTER}.mongodb.net"
        if CLUSTER and (USERNAME or PASSWORD) else
        None
    )

    # Si l'URI est None, retourner localhost
    return mongodb_uri if mongodb_uri else "mongodb://localhost:27017"


class Settings:
    MONGODB_URI: str = get_mongodb_uri()
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "myDatabase")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")


load_dotenv()
settings = Settings()