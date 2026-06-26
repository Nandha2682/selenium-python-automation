import requests
new_post = {
    "title": "QA Automation",
    "body": "Learning API testing",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=new_post   # automatically sets Content-Type: application/json and serializes the dict
)

print("Status Code:", response.status_code)  # expect 201 Created
print("Created Resource:", response.json())