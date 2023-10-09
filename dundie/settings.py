import os

SMTP_HOST = "localhost"
SMTP_PORT = 8025
SMTP_TIMEOUT = 5
EMAIL_FROM = "master@master.com"

DATE_FORMAT = "%d/%m/%Y %H:%M:%S"

ROOT_PATH = os.path.dirname(__file__)
DATABASE_PATH = os.path.join(ROOT_PATH, "..", "assets", "database")
SQL_CON_STR = f"sqlite:///{DATABASE_PATH}"


API_BASE_URL = "https://economia.awesomeapi.com.br/json/last/USD-{currency}"