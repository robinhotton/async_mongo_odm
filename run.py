import subprocess
import os
import sys


def get_venv_scripts(script_name):
    """Renvoie le chemin du répertoire 'Scripts' ou 'bin' de l'environnement virtuel, en fonction du système d'exploitation."""
    if os.name == 'nt':
        # Activation sous Windows
        venv_scripts = os.path.join(".venv", "Scripts", script_name)
    else:
        # Activation sous Linux/Mac
        venv_scripts = os.path.join(".venv", "bin", script_name)
    return venv_scripts


def create_venv():
    """Crée un environnement virtuel '.venv' s'il n'existe pas déjà."""
    if not os.path.exists('.venv'):
        try:
            subprocess.run([sys.executable, "-m", "venv", ".venv"], check=True)
            print("Environnement virtuel créé avec succès.")
        except subprocess.CalledProcessError as e:
            print(f"Échec de la création de l'environnement virtuel : {e}")
            exit(1)
    else:
        print("Environnement virtuel déjà existant.")


def activate_venv():
    """Active l'environnement virtuel '.venv'."""
    venv_activate = get_venv_scripts("activate")
    os.system(venv_activate)


def update_pip():
    """Met à jour pip dans l'environnement virtuel."""
    try:
        venv_python = get_venv_scripts("python")
        subprocess.run([venv_python, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        print("pip a été mis à jour avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Échec de la mise à jour de pip : {e}")
        exit(1)


def install_requirements():
    """Installe les dépendances du projet dans le '.venv' à partir du fichier 'requirements.txt'."""
    try:
        venv_pip = get_venv_scripts("pip")
        subprocess.run([venv_pip, "install", "-r", "requirements.txt"], check=True)
        print("Les dépendances ont été installées avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Échec de l'installation des dépendances : {e}")
        exit(1)
        

def run_uvicorn(host="127.0.0.1", port=8000, log_level="info"):
    """Lance l'application Uvicorn avec les paramètres spécifiés."""
    venv_uvicorn = get_venv_scripts("uvicorn")
    try:
        subprocess.run([
            venv_uvicorn, 
            "app.main:app", 
            "--host", host, 
            "--port", str(port), 
            "--reload", 
            "--log-level", log_level
        ], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Échec de l'exécution de Uvicorn : {e}")
        exit(1)


if __name__ == "__main__":
    create_venv()
    activate_venv()
    update_pip()
    install_requirements()
    run_uvicorn()