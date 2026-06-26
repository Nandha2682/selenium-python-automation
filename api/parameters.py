import requests
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params={"userId": 1}
)
print(response.url)        # see how params got appended to the URL
print(len(response.json()))  # how many posts this user has