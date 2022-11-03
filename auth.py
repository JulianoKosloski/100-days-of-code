import requests as re

# many APIs have paid tiers of API keys so they can sell access to the data they keep

# https://api.openweathermap.org/data/2.5/forecast?lat=-25.480877&lon=-49.304424&appid=94ed3e55937bfc2c54db3a3045fb0f86
weatherEndpoint = "https://api.openweathermap.org/data/2.5/forecast"
myKey = "94ed3e55937bfc2c54db3a3045fb0f86"
lat = -25.480877
lon = -49.304424

params = {
    "lat": lat,
    "lon": lon,
    "appid": myKey 
}

response = re.get(weatherEndpoint, params)
resJSON = response.json()
print("This is the response:\n ", resJSON)



