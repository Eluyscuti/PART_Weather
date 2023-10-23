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

    request_url = "https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=windspeed_{alt},winddirection_{alt}&timezone=America%2FNew_York".format(latitude = str(lat),longitude = str(long), alt = str(str(new_alt)+"m"))

    
    response = requests.get(request_url)
    
    #answer = json.loads(response.json())
    answer = response.json()
    print(answer)

    wind_speed = answer["windspeed_120m"]
    #wind_direction = answer[str("winddirection_{a}m".format(a = new_alt))]

    return wind_speed

    
    


val = get_wind(52.52,13.419998, 101)
print(val)