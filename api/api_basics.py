import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# 1. GET a single post
response = requests.get(f"{BASE_URL}/posts/1")
data = response.json()
print("1. Single post title:", data["title"])

# 2. GET posts filtered by userId
response = requests.get(f"{BASE_URL}/posts", params={"userId": 1})
posts = response.json()
print("2. Number of posts by userId=1:", len(posts))

# 3. POST - create a new post
new_post = {
    "title": "QA Automation",
    "body": "Learning API testing",
    "userId": 1
}
response = requests.post(f"{BASE_URL}/posts", json=new_post)
print("3. POST status:", response.status_code)
print("   Created resource id:", response.json()["id"])

# 4. PUT - full update
updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "Updated body content",
    "userId": 1
}
response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
print("4. PUT status:", response.status_code)

# 5. DELETE
response = requests.delete(f"{BASE_URL}/posts/1")
print("5. DELETE status:", response.status_code)

# 6. GET an invalid post - handle gracefully
response = requests.get(f"{BASE_URL}/posts/9999")
if response.status_code == 200:
    print("6. Success:", response.json())
else:
    print(f"6. Request failed with status {response.status_code}")