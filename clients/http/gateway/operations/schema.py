from enum import StrEnum

from pydantic import BaseModel, Field, HttpUrl, ConfigDict

from tools.fakers import fake

class OperationType(StrEnum):
    FEE= "FEE"
    TOP_UP="TOP_UP"
    PURCHASE="PURCHASE"
    CASHBACK="CASHBACK"
    TRANSFER="TRANSFER"
    BILL_PAYMENT="BILL_PAYMENT"
    CASH_WITHDRAWAL="CASH_WITHDRAWAL"

class OperationStatus(StrEnum):
    FAILED="FAILED"
    COMPLETED="COMPLETED"
    IN_PROGRESS="IN_PROGRESS"
    UNSPECIFIED="UNSPECIFIED"  

class OperationSchema(BaseModel):
    """
    Структура операции.
    """

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")

class OperationReceiptSchema(BaseModel):
    """
    Структура квитанции по операции.
    """ 

    url: HttpUrl
    document: str

class OperationsSummarySchema(BaseModel):
    """
    Структура статистики по операциям.
    """

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")       
class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка по операциям определенного счета.
    """

    account_id: str = Field(alias="accountId")

class GetOperationsResponseSchema(BaseModel):
    """
    Структура ответа на запрос списка операций.
    """

    operations: list[OperationSchema]    

class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    
    account_id: str = Field(alias="accountId")

class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура ответа на запрос статистики по операциям.
    """

    summary: OperationsSummarySchema

class GetOperationReceiptResponseSchema(BaseModel):
    """
    Структура ответа на запрос квитанции по операции.
    """

    receipt: OperationReceiptSchema

class GetOperationResponseSchema(BaseModel):
    """
    Структура ответа на запрос операции по ее id.
    """

    operation: OperationSchema

class MakeFeeOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции комиссии.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeFeeOperationResponseSchema(BaseModel):
    """
    Структура ответа на запрос операции комиссии.
    """
    operation: OperationSchema 

class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Структура для данных для создания операции пополнения.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Структура ответа на запрос операции пополнения.
    """

    operation: OperationSchema

class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции кэшбека.
    """
    model_config = ConfigDict(populate_by_name=True)
    
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Структура ответа на запрос операции кэшбека.
    """

    operation: OperationSchema

class MakeTransferOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции перевода.
    """
    model_config = ConfigDict(populate_by_name=True)
    
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeTransferOperationResponseSchema(BaseModel):
    """
    Структура ответа на запрос операции перевода.
    """

    operation: OperationSchema

class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции покупки.
    """
    model_config = ConfigDict(populate_by_name=True)
    
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str = Field(default_factory=fake.category)

class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Структура ответа на запрос операции покупки.
    """

    operation: OperationSchema

class MakeBillOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции по оплаты счета.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")                         

class MakeBillOperationResponseSchema(BaseModel):
    """
    Структура ответа на запрос операции по оплате счета.
    """

    operation: OperationSchema
class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Структура данных для создания операции снятия наличных.
    """
    model_config = ConfigDict(populate_by_name=True)
    
    status: OperationStatus = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount())
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")

class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Структура ответа на запрос операции снятия наличных.
    """

    operation: OperationSchema