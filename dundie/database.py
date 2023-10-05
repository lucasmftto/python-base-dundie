from sqlmodel import Session, create_engine

from dundie import models
from dundie.settings import SQL_CON_STR

import warnings
from sqlalchemy.exc import SAWarning

warnings.filterwarnings("ignore", category=SAWarning)

engine = create_engine(SQL_CON_STR, echo=False)

models.SQLModel.metadata.create_all(engine)


def get_session(autocommit=False) -> Session:
    return Session(engine, autocommit=autocommit)
