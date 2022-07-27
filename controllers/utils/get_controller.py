import ormar
from functools import wraps
from controllers.utils.entity_not_found import entity_not_found


def get_controller(modelo: ormar.Model, select_related=[]):
    def inner(func):
        @entity_not_found
        @wraps(func)
        async def wrapper(id: int, **kwargs):
            query = modelo.objects
            if len(select_related):
                query = query.select_related(select_related)
            entity = await query.get(id=id)
            return entity
        return wrapper
    return inner