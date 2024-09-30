from fastapi import APIRouter

from .classe_routes     import router as classe_router
from .eleve_routes      import router as eleve_router
from .matiere_routes    import router as matiere_router
from .note_routes       import router as note_router
from .professeur_routes import router as prof_router
from .protected_routes  import router as protected_router
from .trimestre_routes  import router as trimestre_router
from .user_routes       import router as user_router

router = APIRouter()
router.include_router(classe_router)
router.include_router(eleve_router)
router.include_router(matiere_router)
router.include_router(note_router)
router.include_router(prof_router)
router.include_router(protected_router)
router.include_router(trimestre_router)
router.include_router(user_router)
