from clients.http.client import HTTPClient
from typing import TypedDict
from locust.env import Environment
from httpx import Response

from clients.http.gateway.client import build_gateway_http_client, build_gateway_locust_http_client
from clients.http.gateway.cards.schema import (
    IssueVirtualCardRequestSchema,
    IssueVirtualCardResponseSchema,
    IssuePhysicalCardRequestSchema,
    IssuePhysicalCardResponseSchema
)

class CardsGatewayHTTPClient(HTTPClient):

    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: IssueVirtualCardRequestSchema) -> Response:
        """
        Выполянет POST-запрос на выдачу виртуальной карты.

        :param request: Данные для запроса.
        :return: Ответ от сервера (объект httpx.Response).
        """
        
        return self.post(
            "/api/v1/cards/issue-virtual-card", 
            json=request.model_dump(by_alias=True)
            )

    def issue_physical_card_api(self, request: IssuePhysicalCardRequestSchema) -> Response:
        """
        Выполянет POST-запрос на выдачу физической карты.

        :param request: Данные для запроса.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.post(
            "/api/v1/cards/issue-physical-card", 
            json=request.model_dump(by_alias=True)
            )

    # Добавили метод для работы с виртуальной картой
    def issue_virtual_card(self, user_id: str, account_id: str) -> IssueVirtualCardResponseSchema:
        request = IssueVirtualCardRequestSchema(
            userId=user_id, 
            accountId=account_id
        )

        response = self.issue_virtual_card_api(request)

        return IssueVirtualCardResponseSchema.model_validate_json(response.text)
    
    # Добавили метод для работы с физической картой
    def issue_physical_card(self, user_id: str, account_id: str) -> IssuePhysicalCardResponseSchema:
        request = IssuePhysicalCardRequestSchema(
            userId=user_id, 
            accountId=account_id
        )

        response = self.issue_physical_card_api(request)

        return IssuePhysicalCardResponseSchema.model_validate_json(response.text)

    
def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    """
    Функция создает экземпляр CardsGatewayHTTPClient с уже настроенным HTTP клиентом.

    :return: Готовый к использованию CardsGatewayHTTPClient
    """

    return CardsGatewayHTTPClient(client=build_gateway_http_client())

def build_cards_gateway_locust_http_client(environment: Environment) -> CardsGatewayHTTPClient:
    """
    Функция создаёт экземпляр CardsGatewayHTTPClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр CardsGatewayHTTPClient с хуками сбора метрик.
    """
    return CardsGatewayHTTPClient(client=build_gateway_locust_http_client(environment))    