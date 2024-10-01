from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    PROFESSEUR = "PROFESSEUR"
    ELEVE = "ELEVE"