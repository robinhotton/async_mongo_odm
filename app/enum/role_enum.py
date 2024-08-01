from enum import Enum

class RoleEnum(str, Enum):
    ADMIN = "ADMIN"
    PROFSSEUR = "PROFESSEUR"
    ELEVE = "ELEVE"