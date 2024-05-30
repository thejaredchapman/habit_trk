import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
# Please use https://docs.pixe.la/ for documentation

#TODO: Create your own token alphanumeric, Username, and Graph ID. Change parameters.
TOKEN =  "TOKEN"
USERNAME = "USERNAME"
GRAPH_ID = "GRAPH_ID"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# TODO: You will need to update variables per your own standards
graph_config = {
    "id": GRAPH_ID,
    "name" : "name",
    "unit": "unit",
    "type" : "type",
    "color" : "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config)
#print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("Y%m%d"))

pixel_data = {
    "date": today.strftime("Y%m%d"),
    "quantity": "quantity",
}

#response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
#print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "quantity"
}

response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
requests.delete(url=delete_endpoint, headers=headers)
print(response.text)