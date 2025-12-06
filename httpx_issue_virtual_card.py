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


open_debit_card_account_payload = {"userId": create_user_response_data['user']['id']}
open_debit_card_account_res = httpx.post(
    "http://localhost:8003/api/v1/accounts/open-debit-card-account", 
    json=open_debit_card_account_payload
    )
open_debit_card_account_data = open_debit_card_account_res.json()

print("Open debit card account response: ", open_debit_card_account_data)
print("Status Code: ", open_debit_card_account_res.status_code)  

issue_virtual_card_payload = {
  "userId": create_user_response_data['user']['id'],
  "accountId": open_debit_card_account_data['account']['id']
}
issue_virtual_card_res = httpx.post(
    "http://localhost:8003/api/v1/cards/issue-virtual-card",
    json=issue_virtual_card_payload
    )
issue_virtual_card_data = issue_virtual_card_res.json()

print("Open virtual card response: ", issue_virtual_card_data)
print("Status Code: ", issue_virtual_card_res.status_code) 