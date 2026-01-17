from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response

from clients.http.gateway.client import build_gateway_http_client

# Добавили описание структуры карты
class CardDict(TypedDict):
    """
    Описание структуры карты.
    """
    id: str
    pin: str
    cvv: str
    type: str
    status: str
    accountId: str
    cardNumber: str
    cardHolder: str
    expiryDate: str
    paymentSystem: str
class CreateVirtualCardDict(TypedDict):
    """
    Структура данных для запроса на выдачу виртуальной карты.
    """

    userId: str
    accountId: str

class IssueVurtualCardResponseDict(TypedDict):
    """
    Описание структуры ответа выпуска виртуальной карты.
    """
    card: CardDict


class CreatePhysicalCardDict(TypedDict):
    """
    Структура данных для запроса на выдачу физической карты.
    """
    
    userId: str
    accountId: str

class IssuePhysicalCardResponseDict(TypedDict):
    """
    Описание структуры ответа выпуска физической карты.
    """
    card: CardDict       

class CardsGatewayHTTPClient(HTTPClient):

    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: CreateVirtualCardDict) -> Response:
        """
        Выполянет POST-запрос на выдачу виртуальной карты.

        :param request: Данные для запроса.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreatePhysicalCardDict) -> Response:
        """
        Выполянет POST-запрос на выдачу физической карты.

        :param request: Данные для запроса.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.post("/api/v1/cards/issue-physical-card", json=request)

    # Добавили метод для работы с виртуальной картой
    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVurtualCardResponseDict:
        request = CreateVirtualCardDict(
            userId=user_id, 
            accountId=account_id
        )

        response = self.issue_virtual_card_api(request)

        return response.json()
    
    # Добавили метод для работы с физической картой
    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseDict:
        request = CreatePhysicalCardDict(
            userId=user_id, 
            accountId=account_id
        )

        response = self.issue_physical_card_api(request)

        return response.json()

    
def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создает экземпляр CardsGatewayHTTPClient с уже настроенным HTTP клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient
    """

    return CardsGatewayHTTPClient(client=build_gateway_http_client())    