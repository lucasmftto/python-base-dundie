from decimal import Decimal
from typing import Dict, List

import httpx
from dundie.settings import API_BASE_URL
from pydantic import BaseModel, Field


class USDRate(BaseModel):
    code: str = Field(default="USD")
    codein: str = Field(default="USD")
    name: str = Field(default="Dolar/Dolar")
    value: Decimal = Field(alias="high")


def get_rates(currencies: List[str]) -> Dict[str, USDRate]:
    """Get currency rates from API"""
    return_data = {}
    for currency in currencies:
        if currency == "USD":
            return_data[currency] = USDRate(high=1)
        else:
            print(API_BASE_URL.format(currency=currency))
            response = httpx.get(API_BASE_URL.format(currency=currency))
            if response.status_code == 200:
                print(response.json())
                data = response.json()["USD" + currency.upper()]
                return_data[currency] = USDRate(**data)
            else:
                return_data[currency] = USDRate(
                    name="Invalid Currency", high=0
                )

    return return_data
