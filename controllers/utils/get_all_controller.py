import ormar
from functools import wraps
from controllers.utils.entity_not_found import entity_not_found


def get_all_controller(modelo: ormar.Model):
    def inner(func):
        @wraps(func)
        async def wrapper():
                return await modelo.objects.all()
        return wrapper
    return inner