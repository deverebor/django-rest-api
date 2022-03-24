import requests

headers = {'Authorization': 'Bearer 4cd1b38f30f5fcefffea2856d450ecff461ec36f'}
endpoint = "http://localhost:8000/api/products/"

data = {
  "title": "The Catcher in the Rye",
  "price": "12.99",
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())