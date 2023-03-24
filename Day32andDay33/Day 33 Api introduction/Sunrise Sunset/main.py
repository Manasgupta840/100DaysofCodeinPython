import requests

parameters = {
    "lat": 20.5937,
    "lng": 78.9629
}

response = requests.get(f"https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
