import httpx
import time

create_user_payload = {
  "email": f"user.{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

create_user_res = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_res.json()

print("Create user response: ", create_user_response_data)
print("Status Code: ", create_user_res.status_code)

open_credit_card_account_payload = {"user_id":create_user_response_data['user']['id']}

open_credit_card_account_res = httpx.post(
    f"http://localhost:8003/api/v1/accounts/open-credit-card-account", 
    json=open_credit_card_account_payload
    )
open_credit_card_account_data = open_credit_card_account_res.json()

print("Open credit card account response: ", open_credit_card_account_data)
print("Status Code: ", open_credit_card_account_res.status_code)

get_tariff_documents_res= httpx.get(
    f"http://localhost:8003/api/v1/documents/tariff-document/"
    f"{open_credit_card_account_data['account']['id']}"
    )

get_tariff_documents_data = get_tariff_documents_res.json()

print("Get tariff documents response: ", get_tariff_documents_data)
print("Status Code: ", get_tariff_documents_res.status_code)


get_conract_documents_res= httpx.get(
    f"http://localhost:8003/api/v1/documents/contract-document/"
    f"{open_credit_card_account_data['account']['id']}"
    )

get_contract_documents_data = get_conract_documents_res.json()

print("Get contract documents response: ", get_contract_documents_data)
print("Status Code: ", get_conract_documents_res.status_code)