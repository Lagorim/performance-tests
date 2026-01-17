from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict

from clients.http.gateway.client import build_gateway_http_client

class DocumentsDict(TypedDict):
    """
    Описание структуры документа
    """
    url: str
    document: str

class GetTariffDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос получения тарифа по счету
    """
    tariff: DocumentsDict

class GetContractDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа на запрос получения контракта по счету
    """
    contract: DocumentsDict

class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id:str) -> Response:
        """
        Получение тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.get(f"/api/v1/documents/tariff-document/{account_id}")
    
    def get_contract_document_api(self, account_id:str) -> Response:
        """
        Получение контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """

        return self.get(f"/api/v1/documents/contract-document/{account_id}")
    
    #Добавление метода для получения тарифа по счету
    def get_tariff_document(self, account_id:str) -> GetTariffDocumentResponseDict:
        response = self.get_tariff_document_api(account_id)
        return response.json()
    
    #Добавление метода для получения контракта по счету
    def get_contract_document(self, account_id:str) -> GetContractDocumentResponseDict:
        response = self.get_contract_document_api(account_id)
        return response.json()

def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создает экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient
    """

    return DocumentsGatewayHTTPClient(client=build_gateway_http_client()) 