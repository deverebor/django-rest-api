import requests

endpoint = "http://localhost:8000/api/products/"

data = {
  "title": "The Catcher in the Rye",
}

get_response = requests.post(endpoint, data)
print(get_response.json())