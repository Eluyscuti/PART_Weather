import requests
import json

def get_wind(lat, long, actual_altitude):
    possible_altitudes = [10,80,120,180]
    differences = []
    for altitude in possible_altitudes:
        diff =  abs(actual_altitude-altitude)
        differences.append(diff)

    new_alt = possible_altitudes[differences.index(min(differences))] 
    print(new_alt)

    #request_url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=windspeed_{alt},winddirection_{alt}&timezone=America%2FNew_York".format(latitude = str(lat),longitude = str(long), alt = str(str(new_alt)+"m"))
    request_url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=windspeed_10m,winddirection_10m"
    
    response = requests.get(request_url)
    
    #answer = json.loads(response.json())
    answer = response.json()
    #print(answer)
    #print(answer["latitude"])

    wind_speed = answer["current"]["windspeed_{alt}m".format(alt = str(10))]
    
    wind_direction = answer["current"][str("winddirection_{a}m".format(a = 10))]

    return wind_speed, wind_direction

    
    


val = get_wind(52.52,13.419998, 101)
print(val)