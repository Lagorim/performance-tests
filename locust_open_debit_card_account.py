from locust import User, between, task

from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema
from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client

class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
     # Пауза между запросами для каждого виртуального пользователя (в секундах)
    wait_time = between(1, 3)

   # Поле, в котором будет храниться экземпляр нашего API клиента
    users_gateway_client: UsersGatewayHTTPClient
    # Поле, куда мы сохраним ответ после создания пользователя
    create_user_response: CreateUserResponseSchema
    # Поле для хранения аккаунтов
    accounts_gateway_client: AccountsGatewayHTTPClient

    def on_start(self) -> None:
        """
        Метод on_start вызывается один раз при запуске каждой сессии виртуального пользователя.
        Здесь мы создаем нового пользователя, отправляя POST-запрос к /api/v1/users.
        """
        # Шаг 1: создаем API клиент, встроенный в экосистему Locust (с хуками и поддержкой сбора метрик)
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)

        # Шаг 2: создаем пользователя через API
        self.create_user_response = self.users_gateway_client.create_user()

        # Шаг 3: получаем данные аккаунта
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)



    @task
    def open_debit_card(self):

        self.accounts_gateway_client.open_debit_card_account(self.create_user_response.user.id)
