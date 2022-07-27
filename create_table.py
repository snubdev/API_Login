import sqlalchemy
import models.import_models
from databases.core import DatabaseURL
from config import DATABASE_URL, metadata


def configure_bd(database_url = DATABASE_URL):
    engine = sqlalchemy.create_engine(database_url)
    metadata.drop_all(engine)
    metadata.create_all(engine)


if __name__ == "__main__":
    configure_bd()