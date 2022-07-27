import ormar
from functools import wraps
from pydantic import BaseModel

from controllers.utils.entity_not_found import entity_not_found


def patch_controller(modelo: ormar.Model):
    def inner(func):
        @entity_not_found
        @wraps(func)
        async def wrapper(propertis_update: BaseModel, id: int, **kwargs):
                saved_entity = await modelo.objects.get(id=id)
                propertis_update = propertis_update.dict(exclude_unset=True)
                await saved_entity.update(**propertis_update)
                return saved_entity
        return wrapper
    return inner
