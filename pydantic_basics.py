from pydantic import BaseModel, Field
from datetime import date

class CardSchema(BaseModel):
    id: str
    pin: str
    cvv: str
    status: str
    account_id: str = Field(alias='accountId')
    card_number: str = Field(alias='cardNumber')
    card_holder: str = Field(alias='cardHolder')
    expiry_date: str = Field(alias='expiryDate')
    payment_system: str = Field(alias='paymentSystem')

class AccountSchema(BaseModel):
    id: str
    type: str
    cards: list[CardSchema]
    status: str
    balance: float

account_default_model = AccountSchema(
    id="account-id",
    type="deposit",
    status="active",
    balance=1000.00
)

print('Account default model:', account_default_model)