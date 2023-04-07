import requests
import json
import os
city = input("Enter the name of city\n")
#using api from api.weather.com
url = f"https://api.weatherapi.com/v1/current.json?key=a9ec14ad7d8245f08ed181130230604&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)       #converts r from string datatype to dictionary
x = wdic["current"]["temp_c"]   #getting info from dictionary r
print(x)
command = f"spd-say {x}"
os.system(command)
