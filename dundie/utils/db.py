from datetime import datetime
from sqlmodel import Session
from dundie.models import Person

from dundie.utils.email import check_valid_email, send_email
from dundie.utils.user import generate_simple_password
from dundie.settings import DATABASE_PATH, EMAIL_FROM

def add_person(session: Session, instance: Person):
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


def set_initial_password(session: Session, instance: Person):
    """Generated and saves password"""
    db["users"].setdefault(pk, {})
    db["users"][pk]["password"] = generate_simple_password(8)
    return db["users"][pk]["password"]


def set_initial_balance(session: Session, instance: Person):
    """Sets the initial balance for a person."""
    value = 100 if person["role"] == "Manager" else 500
    add_movement(db, pk, value)


def add_movement(session: Session, instance: Person):
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

