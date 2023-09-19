from pydantic import BaseModel, validator
from decimal import Decimal
from datetime import datetime
from dundie.utils.email import check_valid_email

class Person(BaseModel):
    pk: str
    name: str
    dept: str
    role: str
    
    @validator('pk')
    def validate_email(cls, v):
        if not check_valid_email(v):
            raise ValueError(f"{v} is not a valid email")
        return v
    
    def __str__(self):
        return f"{self.name} ({self.role})"
    
class Balance(BaseModel):
    person: Person
    value: Decimal
    
    @validator('value', pre=True)
    def value_logic(cls, v):
        return Decimal(v)
    
    class Config:
        json_encoders = {Person : lambda p: p.pk}

class Movement(BaseModel):
    person: Person
    date: datetime
    actor: str
    value: Decimal