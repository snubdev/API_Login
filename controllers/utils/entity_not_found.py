from fastapi import HTTPException
import ormar
from functools import wraps


def entity_not_found(func):
    @wraps(func)
    async def inner(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ormar.exceptions.NoMatch:
            raise HTTPException(status_code=404, detail="Entidade não encontrada")
    return inner