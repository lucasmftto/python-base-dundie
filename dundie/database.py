import json
from datetime import datetime

from dundie.settings import DATABASE_PATH, EMAIL_FROM
from dundie.utils.email import check_valid_email, send_email
from dundie.utils.user import generate_simple_password

EMPTY_DATABASE = {"people": {}, "balance": {}, "movement": {}, "users": {}}


def connect() -> dict:
    """Connects to the database and returns the database object."""

    try:
        with open(DATABASE_PATH, "r") as file:
            return json.loads(file.read())
    except (json.JSONDecodeError, FileNotFoundError):
        return EMPTY_DATABASE


def commit(db):
    """Commits the database object to the database file."""
    if db.keys() != EMPTY_DATABASE.keys():
        raise ValueError("Invalid database Schema.")

    with open(DATABASE_PATH, "w") as file:
        file.write(json.dumps(db, indent=4))


def add_person(db, pk, data):
    """Saves person data to database.
    - Email is unique (resolved by dictionary hash table)
    - If exists, update, else create
    - Set initial balance (managers = 100, others = 500)
    - Generate a password if user is new and send_email
    """
    if not check_valid_email(pk):
        raise ValueError(f"{pk} is not a valid email")

    table = db["people"]
    person = table.get(pk, {})
    created = not bool(person)
    person.update(data)
    table[pk] = person
    if created:
        set_initial_balance(db, pk, person)
        password = set_initial_password(db, pk)
        send_email(EMAIL_FROM, pk, "Your dundie password", password)
        # TODO: Encrypt and send only link not password
    return person, created


def set_initial_password(db, pk):
    """Generated and saves password"""
    db["users"].setdefault(pk, {})
    db["users"][pk]["password"] = generate_simple_password(8)
    return db["users"][pk]["password"]


def set_initial_balance(db, pk, person):
    """Sets the initial balance for a person."""
    value = 100 if person["role"] == "Manager" else 500
    add_movement(db, pk, value)


def add_movement(db, pk, value, actor="SYSTEM"):
    """Adds a movement to the database."""
    movement = db["movement"].setdefault(pk, [])
    movement.append(
        {
            "value": value,
            "date": datetime.now().isoformat(),
            "actor": actor,
        }
    )
    db["balance"][pk] = sum([item["value"] for item in movement])
