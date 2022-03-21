import requests

endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"title": "Makalister Renton","content": "Hello world", "price": 100})
print(get_response.json())