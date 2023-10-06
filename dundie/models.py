from datetime import datetime
from decimal import Decimal
from typing import Optional

from dundie.utils.email import check_valid_email
from dundie.utils.user import generate_simple_password
from pydantic import validator, condecimal
from sqlmodel import Field, SQLModel, Relationship


class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    email: str = Field(nullable=False, index=True)
    name: str = Field(nullable=False)
    dept: str = Field(nullable=False, index=True)
    role: str = Field(nullable=False)

    balance: "Balance" = Relationship(back_populates="person")
    movement: "Movement" = Relationship(back_populates="person")
    user: "User" = Relationship(back_populates="person")

    @validator("email")
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise ValueError(f"{v} is not a valid email")
        return v

    def __str__(self):
        return f"{self.name} ({self.role}) - {self.email} - {self.dept}"


class Balance(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    value: condecimal(decimal_places=3) = Field(default=0)

    person: Person = Relationship(back_populates="balance")

    @validator("value", pre=True)
    def value_logic(cls, v):
        return Decimal(v)

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class Movement(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    date: datetime = Field(default_factory=lambda : datetime.now())
    actor: str = Field(nullable=False, index=True)
    value: condecimal(decimal_places=3) = Field(default=0)

    person: Person = Relationship(back_populates="movement")

    class Config:
        json_encoders = {Person: lambda p: p.pk}


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    person_id: int = Field(foreign_key="person.id")
    password: str = Field(default_factory=generate_simple_password)

    person: Person = Relationship(back_populates="user")

    class Config:
        json_encoders = {Person: lambda p: p.pk}