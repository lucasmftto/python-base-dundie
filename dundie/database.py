from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar

from dundie import models
from dundie.settings import SQL_CON_STR

import warnings
from sqlalchemy.exc import SAWarning

SelectOfScalar.inherit_cache = True
Select.inherit_cache = True

warnings.filterwarnings("ignore", category=SAWarning)

engine = create_engine(SQL_CON_STR, echo=False)

models.SQLModel.metadata.create_all(engine)


def get_session() -> Session:
    return Session(engine)
