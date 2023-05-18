from fastapi import APIRouter
from app.api.routes import mailings, messages, clients

router = APIRouter()

router.include_router(clients.router, prefix="/сlients", tags=["сlients"])
router.include_router(mailings.router, prefix="/mailings", tags=["mailings"])
router.include_router(messages.router, prefix="/messages", tags=["messages"])
