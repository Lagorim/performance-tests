from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response

class GetOperationsViewQueryDict(TypedDict):
    """
    Структура данных для получения списка по операциям определенного счета.
    """

    accountId: str

class GetOperationsSummaryViewQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    
    accountId: str

class MakeFreeOperationViewRequestDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """

    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationViewRequestDict(TypedDict):
    """
    Структура для данных для создания операции пополнения.
    """

    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationViewRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбека.
    """
    
    status: str
    amount: float
    cardId: str
    accountId: str    

class MakeTransferOperationViewRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """
    
    status: str
    amount: float
    cardId: str
    accountId: str

class MakePurchaseOperationViewRequestDict(TypedDict):
    """
    Структура данных для создания операции покупки.
    """
    
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str 

class MakeBillOperationViewRequestDict(TypedDict):
    """
    Структура данных для создания операции по оплаты счета.
    """

    status: str
    amount: float
    cardId: str
    accountId: str                          

class MakeCashWithdrawalOperationViewRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных.
    """
    
    status: str
    amount: float
    cardId: str
    accountId: str 

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """
    
    def get_operations_api(self, query:GetOperationsViewQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о операциях с определенным счетом.
        """
        
        return self.get("/api/v1/operations", params=query)
    
    def get_operations_summary_api(self, query:GetOperationsSummaryViewQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение статистики по операциям для определенного счета

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response статистика по операциям с определенным счетом.
        """

        return self.get("/api/v1/operations/operations-summary", params=query)
    
    def get_operation_receipt_api(self, operation_id:str) -> Response:
        """
        Выполняет GET-запрос на получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")
    
    def get_operation_api(self, operation_id:str) -> Response:
        """
        Выполняет GET-запрос на получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.get(f"/api/v1/operations/{operation_id}")
    
    def make_fee_operation_api(self, request:MakeFreeOperationViewRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-fee-operation", json=request)
    
    def make_top_up_operation_api(self, request:MakeTopUpOperationViewRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции пополнения.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.post("/api/v1/operations/make-top-up-operation", json=request)
    
    def make_cashback_operation_api(self, request:MakeCashbackOperationViewRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции кэшбека.

        :param request: Словарь с данными для создания операции кэшбека.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-cashback-operation", json=request)
    
    def make_transfer_operation_api(self, request:MakeTransferOperationViewRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции перевода.

        :param request: Словарь с данными для создания операции перевода.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-transfer-operation", json=request)
    
    def make_purchase_operation_api(self, request:MakePurchaseOperationViewRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции покупки.

        :param request: Словарь с данными для создания операции покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-purchase-operation", json=request)
    
    def make_bill_payment_operation_api(self, request:MakeBillOperationViewRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции оплаты счета.

        :param request: Словарь с данными для создания операции оплаты счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)
    
    def make_cash_withdrawal_operation_api(self, request:MakeCashWithdrawalOperationViewRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции снятия наличных.

        :param request: Словарь с данными для создания операции снятия наличных.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)