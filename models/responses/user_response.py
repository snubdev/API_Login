from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    nome: str
    email: str