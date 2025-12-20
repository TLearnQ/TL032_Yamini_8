import requests
api_url = "https://httpbin.org/post"
headers = {
    "Authorization": "Bearer mytoken",
    "Content-Type": "application/json"
}
payload = {
    "x": 10,
    "y": 20,
    "z": 30
}
response = requests.post(api_url, json=payload, headers=headers)
response_data = response.json()
recieved_data = response_data.get("json", {})
matching_keys = [key for key in payload if key in recieved_data and payload[key] == recieved_data[key]]
print('The count of the Matching keys is :', len(matching_keys), 'and the matching keys are :', matching_keys)

