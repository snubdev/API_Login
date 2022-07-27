from typing import List
from fastapi import APIRouter, Form, HTTPException, Depends
from controllers.utils.delete_controller import delete_controller
from controllers.utils.get_all_controller import get_all_controller
from controllers.utils.get_controller import get_controller
from controllers.utils.patch_controller import patch_controller
from controllers.depends.usuario import get_user_logged
from models.requests.user_update import UserUpdateRequest
from models.requests.user_create import UserCreateRequest
from models.responses.user_response import UserResponse
from models.user import User
from security import verify_password, create_token_jwt

router = APIRouter()


@router.post("/", response_model=UserResponse)
async def add_item(create_request: UserCreateRequest):
    atributos = create_request.dict(exclude_unset=True)
    usuario = User(**atributos)
    return await usuario.save()


@router.get("/", response_model=List[UserResponse])
@get_all_controller(User)
async def list_item():
    pass


@router.get("/{id}", response_model=UserResponse)
@get_controller(User)
async def get_user(id: int):
    pass


@router.patch("/{id}", response_model=UserResponse)
@patch_controller(User)
async def path_user(propriedades_atualizacao: UserUpdateRequest, id: int):
    pass


@router.delete("/{id}")
@delete_controller(User)
async def delete_user(id: int, usuario_logado: User = Depends(get_user_logged)):
    pass


@router.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    user = await User.objects.get_or_none(email=username)
    if not user or not verify_password(password, user.hash_password):
        raise HTTPException(status_code=403, detail="Email ou nome de usuário incorretos")
    return {
        "access_token": create_token_jwt(user.id),
        "token_type": "bearer",
    }