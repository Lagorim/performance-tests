import httpx
import time

create_user_pauload = {
  "email": f"user.{time.time()}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string",
  "phoneNumber": "string"
}

create_user_res = httpx.post("http://localhost:8003/api/v1/users", json=create_user_pauload)
create_user_response_data = create_user_res.json()

print("Create user response: ", create_user_response_data)
print("Status Code: ", create_user_res.status_code)

get_user_res = httpx.get(f"http://localhost:8003/api/v1/users/{create_user_response_data}['user']['id']")
get_user_response_data = get_user_res.json()
print("Get user response: ", get_user_response_data)
print("Status Code: ", create_user_res.status_code)