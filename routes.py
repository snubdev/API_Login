from fastapi import APIRouter
from controllers import usuario_controller as user

router = APIRouter()

# rotas

router.include_router(user.router, prefix='/usuarios', tags=['User'])