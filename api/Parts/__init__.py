from fastapi import APIRouter
from MyListAnalyzerAPI.routes import application_router as m_l_a_router

application_router = APIRouter()
application_router.include_router(m_l_a_router)
