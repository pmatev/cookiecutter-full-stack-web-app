from fastapi import Depends, FastAPI
from sqlmodel import Session, select, text

from app.database import get_db
from app.models import User

app = FastAPI()


def get_user(session: Session = Depends(get_db)) -> User | None:
    user = session.exec(select(User)).first()
    return user


@app.get("/health")
async def get_health(session: Session = Depends(get_db)):
    session.exec(select(1)).one()
    return {
        'ok': True
    }

@app.get("/v1/user")
async def get_user(user: User = Depends(get_user)):
    return user
