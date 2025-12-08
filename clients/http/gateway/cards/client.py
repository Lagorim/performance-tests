from clients.http.client import HTTPClient
from typing import TypedDict
from httpx import Response

class CreateVirtualPhysicalCardDict(TypedDict):
    userId: str
    accountId: str

class CardsGatewayHTTPClient(HTTPClient):

    def issue_virtual_card_api(self, request: CreateVirtualPhysicalCardDict) -> Response:
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreateVirtualPhysicalCardDict) -> Response:
        return self.post("/api/v1/cards/issue-physical-card", json=request)