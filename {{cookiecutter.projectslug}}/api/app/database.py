from app.config import settings
from sqlmodel import Session, create_engine

engine = create_engine(settings.database_url, echo=False)


def get_db():
    with Session(engine) as session:
        yield session

