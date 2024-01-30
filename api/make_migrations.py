
import os
from sqlalchemy import MetaData
from alembic.config import Config
from sqlmodel import SQLModel

from app.models import User
from app.database import engine


def generate_migration_script(model: SQLModel):
    # Create a metadata object for the current database schema
    current_metadata = MetaData()
    current_metadata.reflect(bind=engine)
    print('current_metadata', current_metadata)

    # Create a metadata object for the model schema
    model_metadata = model.schema_json()
    print('model_metadata', model_metadata)


# Example usage
if __name__ == "__main__":
    migration_directory = "./db/migrations"  # Replace with your migration directory

    result = generate_migration_script(User)
    print(f"Migration script generated at: {result}")
