import requests

response = requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=windspeed_180m,winddirection_180m&timezone=America%2FNew_York")

print(response.json())