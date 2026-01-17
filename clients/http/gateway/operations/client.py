from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response

from clients.http.gateway.client import build_gateway_http_client

class OperationDict(TypedDict):
    """
    Структура операции.
    """

    id: str
    type: str
    status: str
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str

class OperationReceiptDict(TypedDict):
    """
    Структура квитанции по операции.
    """ 

    url: str
    document: str

class OperationsSummaryDict(TypedDict):
    """
    Структура статистики по операциям.
    """

    spentAmount: float
    receivedAmount: float
    cashbackAmount: float       
class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка по операциям определенного счета.
    """

    accountId: str

class GetOperationsResponseDict(TypedDict):
    """
    Структура ответа на запрос списка операций.
    """

    operations: list[OperationDict]    

class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета.
    """
    
    accountId: str

class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа на запрос статистики по операциям.
    """

    summary: OperationsSummaryDict

class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура ответа на запрос квитанции по операции.
    """

    receipt: OperationReceiptDict

class GetOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос операции по ее id.
    """

    operation: OperationDict

class MakeFeeOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции комиссии.
    """

    status: str
    amount: float
    cardId: str
    accountId: str

class MakeFeeOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос операции комиссии.
    """
    operation: OperationDict  

class MakeTopUpOperationRequestDict(TypedDict):
    """
    Структура для данных для создания операции пополнения.
    """

    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTopUpOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос операции пополнения.
    """

    operation: OperationDict

class MakeCashbackOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции кэшбека.
    """
    
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeCashbackOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос операции кэшбека.
    """

    operation: OperationDict

class MakeTransferOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции перевода.
    """
    
    status: str
    amount: float
    cardId: str
    accountId: str

class MakeTransferOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос операции перевода.
    """

    operation: OperationDict

class MakePurchaseOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции покупки.
    """
    
    status: str
    amount: float
    cardId: str
    accountId: str
    category: str 

class MakePurchaseOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос операции покупки.
    """

    operation: OperationDict

class MakeBillOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции по оплаты счета.
    """

    status: str
    amount: float
    cardId: str
    accountId: str                          

class MakeBillOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос операции по оплате счета.
    """

    operation: OperationDict
class MakeCashWithdrawalOperationRequestDict(TypedDict):
    """
    Структура данных для создания операции снятия наличных.
    """
    
    status: str
    amount: float
    cardId: str
    accountId: str 

class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Структура ответа на запрос операции снятия наличных.
    """

    operation: OperationDict

class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """
    
    def get_operations_api(self, query:GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций для определенного счета

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response с данными о операциях с определенным счетом.
        """
        
        return self.get("/api/v1/operations", params=query)
    
    def get_operations_summary_api(self, query:GetOperationsSummaryQueryDict) -> Response:
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
    
    def make_fee_operation_api(self, request:MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции комиссии.

        :param request: Словарь с данными для создания операции комиссии.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-fee-operation", json=request)
    
    def make_top_up_operation_api(self, request:MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции пополнения.

        :param request: Словарь с данными для создания операции пополнения.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.post("/api/v1/operations/make-top-up-operation", json=request)
    
    def make_cashback_operation_api(self, request:MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции кэшбека.

        :param request: Словарь с данными для создания операции кэшбека.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-cashback-operation", json=request)
    
    def make_transfer_operation_api(self, request:MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции перевода.

        :param request: Словарь с данными для создания операции перевода.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-transfer-operation", json=request)
    
    def make_purchase_operation_api(self, request:MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции покупки.

        :param request: Словарь с данными для создания операции покупки.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-purchase-operation", json=request)
    
    def make_bill_payment_operation_api(self, request:MakeBillOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции оплаты счета.

        :param request: Словарь с данными для создания операции оплаты счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)
    
    def make_cash_withdrawal_operation_api(self, request:MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос на создание операции снятия наличных.

        :param request: Словарь с данными для создания операции снятия наличных.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=request)
    
    #Добавляем методы для работы с операциями
    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()
    
    #Добавляем методы для работы с статистикой по операциям
    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()
    
    #Добавляем методы для работы с чеком по операции
    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        response = self.get_operation_receipt_api(operation_id)
        return response.json()
    
    #Добавляем метод для работы с операциями по ID
    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        response = self.get_operation_api(operation_id)
        return response.json()
    
    #Добавляем методы для работы с операциями комиссии
    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
        status="COMPLETED",
        amount=55.77,
        cardId=card_id,
        accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()
    
    #Добавляем методы для работы с операциями пополнения
    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
        status="COMPLETED",
        amount=100.45,
        cardId=card_id,
        accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()
    
    #Добавляем методы для работы с операциями кэшбека
    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
        status="COMPLETED",
        amount=11.15,
        cardId=card_id,
        accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()
    
    #Добавляем методы для работы с операциями перевода
    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
        status="COMPLETED",
        amount=190.45,
        cardId=card_id,
        accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()
    
    #Добавляем методы для работы с операциями покупки
    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
        status="COMPLETED",
        amount=167.45,
        cardId=card_id,
        accountId=account_id
        )
        response = self.make_purchase_operation_api(request)
        return response.json()
    
    #Добавляем методы для работы с операциями оплаты счета
    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillOperationResponseDict:
        request = MakeBillOperationRequestDict(
        status="COMPLETED",
        amount=106.45,
        cardId=card_id,
        accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()
    
    #Добавляем методы для работы с операциями снятия наличных
    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
        status="COMPLETED",
        amount=1000.00,
        cardId=card_id,
        accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()
    
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создает экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP клиентом.

    :return: Готовый к использованию OperationsGatewayHTTPClient
    """

    return OperationsGatewayHTTPClient(client=build_gateway_http_client())     