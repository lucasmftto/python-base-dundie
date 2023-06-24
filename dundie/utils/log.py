import logging
import os
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG").upper()
log = logging.Logger("DUNDIE", LOG_LEVEL)
# formatacao
fmt = logging.Formatter(
    "%(asctime)s %(name)s %(levelname)s "
    + " l:%(lineno)d f:%(filename)s: %(message)s"
)


def get_logger(logfile="dundie.log"):
    # nossa instancia

    # level
    # ch = logging.StreamHandler() #Cosole/ terminal/ sdterr
    # ch.setLevel(log_level)
    fh = handlers.RotatingFileHandler(
        logfile, maxBytes=700, backupCount=10  # 10**6,
    )
    fh.setLevel(LOG_LEVEL)

    # ch.setFormatter(fmt)
    fh.setFormatter(fmt)

    # destino
    # log.addHandler(ch)
    log.addHandler(fh)

    return log
