import requests
import json
import os

def weather_api(url):
    query ={}
    try:
        response = requests.get(url,timeout=5)
        if response.status_code == 200:
            data = response.json()
            try:
                query["city"] = data.get("name")
                query["temp"] = data["main"]["temp"]
                query["description"] = data["weather"][0]["description"]
            except KeyError:
                print ("unexpectedd API response structure")
                return {}
        
            folder = os.path.dirname(__file__)
            output = os.path.join(folder,"weather.json")
            
            with open(output,"w") as f:
                json.dump(query,f)

    except requests.exceptions.Timeout:
        print ("timeout error")
        return {}
    except requests.exceptions.JSONDecodeError:
        print ("Json file problem")
        return{}
    return query

url ="https://api.openweathermap.org/data/2.5/weather?q=Rawang,MY&appid=a2589b903cb4c2354aeff96dc64eb2a9&units=metric"
file = r"03-coffee-sales-etl-pipeline\v2_api.py"
print(weather_api(url))