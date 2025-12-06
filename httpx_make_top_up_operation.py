import httpx
import time

create_user_payload = {
  "email": f"user.{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

create_user_res = httpx.post("http://localhost:8003/api/v1/users", 
                             json = create_user_payload
                             )
create_user_response_data = create_user_res.json()


# open_credit_card_account_payload = {
#     "userId": create_user_response_data['user']['id']
#     }

print("Create user response: ", create_user_response_data)
print("Status Code: ", create_user_res.status_code)

open_debit_card_account_payload = {"user_id":create_user_response_data['user']['id']}

open_debit_card_account_res = httpx.post(
    f"http://localhost:8003/api/v1/accounts/open-debit-card-account", 
    json=open_debit_card_account_payload
    )
open_debit_card_account_data = open_debit_card_account_res.json()


make_top_up_operation_payload = {
  "status": "COMPLETED",
  "amount": 1500,
  "cardId": open_debit_card_account_data["account"]["cards"][0]["id"],
  "accountId": open_debit_card_account_data["account"]["id"]
}
make_top_up_operation_res = httpx.post("http://localhost:8003/api/v1/operations/make-top-up-operation", 
                                       json = make_top_up_operation_payload)

make_top_up_operation_data = make_top_up_operation_res.json()

print("Make top up operation response: ", make_top_up_operation_data)
print("Status Code: ", make_top_up_operation_res.status_code)