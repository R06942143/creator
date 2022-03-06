from fastapi import APIRouter

from app.api.api_v1.endpoints import login, utils, creator, profanity

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(creator.router, prefix="/creator", tags=["creator"])
api_router.include_router(profanity.router, prefix="/profanity", tags=["profanity"])

# api_router.include_router()
# api_router.include_router(link.router, prefix="/link", tags=["link"])
# api_router.include_router(bank.router, prefix="/bank", tags=["bank"])
# api_router.include_router(benefitsharing.router, prefix="/benefitsharing", tags=["benefitsharing"])