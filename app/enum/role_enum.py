from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    PROFESSEUR = "PROFESSEUR"  # Correction du nom ici pour "PROFESSEUR"
    ELEVE = "ELEVE"