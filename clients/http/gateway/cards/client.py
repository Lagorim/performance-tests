from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response

class CreateVirtualCardDict(TypedDict):
    """
    Структура данных для запроса на выдачу виртуальной карты.
    """

    userId: str
    accountId: str

class CreatePhysicalCardDict(TypedDict):
    """
    Структура данных для запроса на выдачу физической карты.
    """
    
    userId: str
    accountId: str    

class CardsGatewayHTTPClient(HTTPClient):

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