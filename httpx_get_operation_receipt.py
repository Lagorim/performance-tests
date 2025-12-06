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

make_purchase_operation_payload = {
  "status": "IN_PROGRESS",
  "amount": 77.99,
  "cardId": open_credit_card_account_data["account"]["cards"][0]["id"],
  "accountId": open_credit_card_account_data["account"]["id"],
  "category": "taxi"
}

make_purchase_operation_res = httpx.post("http://localhost:8003/api/v1/operations/make-purchase-operation",
                                          json=make_purchase_operation_payload)

make_purcahse_operation_data = make_purchase_operation_res.json()

print("Make purchase operation response: ", make_purcahse_operation_data)
print("Status Code: ", make_purchase_operation_res.status_code)

