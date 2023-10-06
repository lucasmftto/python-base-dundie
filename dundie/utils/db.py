from sqlmodel import Session, select
from dundie.models import Person, User, Movement, Balance
from typing import Optional

from dundie.utils.email import check_valid_email, send_email
from dundie.settings import EMAIL_FROM


def add_person(session: Session, instance: Person):
    """Saves person data to database.
    - Email is unique (resolved by dictionary hash table)
    - If exists, update, else create
    - Set initial balance (managers = 100, others = 500)
    - Generate a password if user is new and send_email
    """

    if not check_valid_email(instance.email):
        raise ValueError(f"{instance.email} is not a valid email")

    existing = session.exec(
        select(Person).where(Person.email == instance.email)
    ).first()

    created = existing is None

    if created:
        session.add(instance)
        set_initial_balance(session, instance)
        password = set_initial_password(session, instance)
        send_email(
            EMAIL_FROM, instance.email, "Your dundie password", password
        )
        return instance, created
    else:
        existing.dept = instance.dept
        existing.role = instance.role
        session.add(existing)
        return instance, created


def set_initial_password(session: Session, instance: Person):
    """Generated and saves password"""
    user = User(person=instance)
    session.add(user)
    return user.password


def set_initial_balance(session: Session, person: Person):
    """Sets the initial balance for a person."""
    value = 100 if person.role == "Manager" else 500
    add_movement(session, person, value)


def add_movement(
    session: Session,
    person: Person,
    value: int,
    actor: Optional[str] = "system",
):
    """Adds a movement to the database."""
    movement = Movement(person=person, value=value, actor=actor)
    session.add(movement)

    movements = session.exec(select(Movement).where(Movement.person == person))

    total = sum([m.value for m in movements])

    existing = session.exec(
        select(Balance).where(Balance.person == person)
    ).first()

    if existing:
        existing.value = total
        session.add(existing)
    else:
        session.add(Balance(person=person, value=total))
