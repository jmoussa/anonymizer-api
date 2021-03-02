from fastapi import APIRouter

from api.auth import router as auth_router
from api.anonymize import router as anon_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(anon_router)
