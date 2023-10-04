from sqlmodel import Session, create_engine

from dundie import models
from dundie.settings import SQL_CON_STR

engine = create_engine(SQL_CON_STR, echo=False)

models.SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)