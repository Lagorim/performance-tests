from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client, build_gateway_locust_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import GetOperationReceiptRequest, GetOperationReceiptResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import GetOperationsSummaryRequest, GetOperationsSummaryResponse
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import MakeFeeOperationRequest, MakeFeeOperationResponse
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationRequest, MakeTopUpOperationResponse
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import MakeCashbackOperationRequest, MakeCashbackOperationResponse
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import MakeCashbackOperationRequest, MakeCashbackOperationResponse
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import MakeTransferOperationRequest, MakeTransferOperationResponse
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import MakeTransferOperationRequest, MakeTransferOperationResponse
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import MakePurchaseOperationRequest, MakePurchaseOperationResponse
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import MakeBillPaymentOperationRequest, MakeBillPaymentOperationResponse
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import MakeCashWithdrawalOperationRequest, MakeCashWithdrawalOperationResponse

from tools.fakers import fake
from contracts.services.operations.operation_pb2 import OperationStatus

from locust.env import Environment

class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет высокоуровневые методы для работы с операциями.
    """

    def __init__(self, channel: Channel):

        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)

        self.stub = OperationsGatewayServiceStub(channel)

    def get_operation_api(self, request:GetOperationRequest) -> GetOperationResponse:
        """
        Получение операции по идентификатору.

        :param request: Запрос на получение операции.
        :return: Ответ с информацией о полученной операции.

        """
        return self.stub.GetOperation(request)
    
    def get_operation_receipt_api(self, request:GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Получение квитанции о выполнении операции по идентификатору.

        :param request: Запрос на получение квитанции о выполнении операции.
        :return: Ответ с информацией о квитанции о выполнении операции.
        
        """
        return self.stub.GetOperationReceipt(request)
    
    def get_operations_api(self, request:GetOperationsRequest) -> GetOperationsResponse:
        """
        Получение списка операций по фильтру.

        :param request: Запрос на получение списка операций.
        :return: Ответ с информацией о полученных опер
    
        """
        return self.stub.GetOperations(request)
    
    def get_operations_summary_api(self, request:GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Получение сводной информации об операциях по фильтру.

        :param request: Запрос на получение сводной информации об операциях.
        :return: Ответ с информацией о сводной информации об операциях.

        """
        
        return self.stub.GetOperationsSummary(request)
    
    def make_fee_operation_api(self, request:MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Создание операции начисления комиссии.

        :param request: Запрос на получение операции начисления комиссии.
        :return: Ответ с информацией о полученной операции начисления комиссии.

        """

        return self.stub.MakeFeeOperation(request)
    
    def make_top_up_operation_api(self, request:MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Создание операции пополнения баланса

        :param request: Запрос на получение операции пополнения баланса.
        :return: Ответ с информацией о полученной операции пополнения баланса.

        """

        return self.stub.MakeTopUpOperation(request)
    
    def make_cashback_operation_api(self, request:MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Создание операции возврата

        :param request: Запрос на получение операции возврата.
        :return: Ответ с информацией о полученной операции возврата.

        """

        return self.stub.MakeCashbackOperation(request)
    
    def make_transfer_operation_api(self, request:MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Создание операции перевода

        :param request: Запрос на получение операции перевода.
        :return: Ответ с информацией о полученной операции перевода.

        """

        return self.stub.MakeTransferOperation(request)
    
    def make_purchase_operation_api(self, request:MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Создание операции покупки

        :param request: Запрос на создание операции покупки
        :return: Ответ с информацией о сожданной операции покупки
        """

        return self.stub.MakePurchaseOperation(request)
    
    def make_bill_payment_operation_api(self, request:MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        Создание операции оплаты по счету

        :param request: Запрос на создание операции оплаты по счету
        :return: Ответ с информацией о созданной операции оплаты по счету
        """

        return self.stub.MakeBillPaymentOperation(request)
    
    def make_cash_withdrawal_operation_api(self, request:MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        Создание операции снятия наличных денег

        :param request: Запрос на создание операции снятия наличных денег
        :return: Ответ с информацией о созданной операции снятия наличных денег
        """

        return self.stub.MakeCashWithdrawalOperation(request)
    
    def get_operation(self, operation_id:str) -> GetOperationResponse:
        """
        Получение операции по идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ с информацией о полученной операции.
        """

        request = GetOperationRequest(operation_id=operation_id)
        return self.get_operation_api(request)
    
    def get_operation_receipt(self, operation_id:str) -> GetOperationReceiptResponse:
        """
        Получение квитанции о выполнении операции по идентификатору.

        :param operation_id: Идентификатор операции.
        :return: Ответ с информацией о квитанции о выполнении операции.
        """

        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)
    
    def get_operations(self, account_id:str) -> GetOperationsResponse:
        """
        Получение списка операций по идентификатору аккаунта

        :param account_id: Идентификатор аккаунта
        :return: Ответ с информацией о полученных операциях
        """

        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request)
    
    def get_operations_summary(self, account_id:str) -> GetOperationsSummaryResponse:
        """
        Получение сводной информации об операциях по идентификатору аккаунта

        :param account_id: Идентификатор аккаунта
        :return: Ответ с информацией о сводной информации об операциях
        """

        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)
    
    def make_fee_operation(self, card_id:str, account_id:str) -> MakeFeeOperationResponse:
        """
        Получение операции начисления комиссии

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        """

        request = MakeFeeOperationRequest(
            status = fake.proto_enum(OperationStatus),
            amount = fake.amount(),
            card_id=card_id, 
            account_id=account_id
        )
        return self.make_fee_operation_api(request)
    
    def make_top_up_operation(self, card_id:str, account_id:str) -> MakeTopUpOperationResponse:
        """
        Получение операции пополнения баланса

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        """

        request = MakeTopUpOperationRequest(
            status = fake.proto_enum(OperationStatus),
            amount = fake.amount(),
            card_id=card_id, 
            account_id=account_id
        )
        return self.make_top_up_operation_api(request)
    
    def make_cashback_operation(self, card_id:str, account_id:str) -> MakeCashbackOperationResponse:
        """
        Получение операции возврата

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        """

        request = MakeCashbackOperationRequest(
            status = fake.proto_enum(OperationStatus),
            amount = fake.amount(),
            card_id=card_id, 
            account_id=account_id
        )
        return self.make_cashback_operation_api(request)
    
    def make_transfer_operation(self, card_id:str, account_id:str) -> MakeTransferOperationResponse:
        """
        Получение операции перевода

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        """

        request = MakeTransferOperationRequest(
            status = fake.proto_enum(OperationStatus),
            amount = fake.amount(),
            card_id=card_id, 
            account_id=account_id
        )
        return self.make_transfer_operation_api(request)
    
    def make_purchase_operation(self, card_id:str, account_id:str) -> MakePurchaseOperationResponse:
        """
        Получение операции покупки

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        """

        request = MakePurchaseOperationRequest(
            status = fake.proto_enum(OperationStatus),
            amount = fake.amount(),
            card_id=card_id, 
            account_id=account_id,
            category=fake.category()
        )
        return self.make_purchase_operation_api(request)
    
    def make_bill_payment_operation(self, card_id:str, account_id:str) -> MakeBillPaymentOperationResponse:
        """
        Получение операции оплаты по счету
        
        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        """

        request = MakeBillPaymentOperationRequest(
            status = fake.proto_enum(OperationStatus),
            amount = fake.amount(),
            card_id=card_id, 
            account_id=account_id
        )
        return self.make_bill_payment_operation_api(request)
    
    def make_cash_withdrawal_operation(self, card_id:str, account_id:str) -> MakeCashWithdrawalOperationResponse:
        """
        Получение операции снятия наличных денег

        :param card_id: Идентификатор карты
        :param account_id: Идентификатор аккаунта
        """

        request = MakeCashWithdrawalOperationRequest(
            status = fake.proto_enum(OperationStatus),
            amount = fake.amount(),
            card_id=card_id, 
            account_id=account_id
        )
        return self.make_cash_withdrawal_operation_api(request)




def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client()) 

def build_operations_gateway_locust_grpc_client(environment: Environment) -> OperationsGatewayGRPCClient:
    """
    Функция создаёт экземпляр OperationsGatewayGRPCClient адаптированного под Locust.

    Клиент автоматически собирает метрики и передаёт их в Locust через хуки.
    Используется исключительно в нагрузочных тестах.

    :param environment: объект окружения Locust.
    :return: экземпляр OperationsGatewayGRPCClient с хуками сбора метрик.
    """

    return OperationsGatewayGRPCClient(channel=build_gateway_locust_grpc_client(environment))       


