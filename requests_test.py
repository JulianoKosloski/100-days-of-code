import requests as re

url = "http://api.open-notify.org/iss-now.json" #get iss position data
response = re.get(url)
response.raise_for_status()

print(response.status_code)

data = response.json()

print(data)

# ------------------

# lat 25º25'48'' south
# long 	49º16'15 west

url = "http://api.sunrise-sunset.org/json"
lat = -25.480877 #curitiba
lng = -49.304424
params = {"lat": lat, "lng": lng, "formatted": 0}
response = re.get(url, params)
response.raise_for_status()

print(response.status_code)
print(response.json())

# if I was doing this through an url: "http://api.sunrise-sunset.org/json?lat=2321312&lng=321321321"
# 200 response code = success
# 404 response code = doesn't exist
# 1xx response code = something wrong is happening
# 3xx response code = no permission
# 4xx response code = user/request error
# 5xx response code = server problem