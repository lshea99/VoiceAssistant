import requests
import draw
import json

api_key = "599eb04637a023fbf1f071dad96b772b"
root_url = "http://api.openweathermap.org/data/2.5/weather?"

# Input the City name for which we need the weather data
# city_name = input("Please Enter The City Name : ")

def rain(city_name):

    state_code = "US-PA"
    zipcode = 15701
    # Building the final url for the API call
    # url = f"{root_url}appid={api_key}&q={city_name},{state_code},{zipcode}&units=imperial"
    url = f"{root_url}zip={zipcode}&appid={api_key}&units=imperial"
    # sending a get request at the url
    r = requests.get(url)
    # storing the returned json data into a variable
    data = r.json()

    if data['cod'] == 200:
        
        temp = data['main']['temp']
        
        pressure = data['main']['pressure']
        
        humidity = data['main']['humidity']
        
        descr = data['weather'][0]['description']
        
        wind = data['wind']['speed']

        #print(f"City Name : {city_name}")
        # draw.display(f"In {city_name}, the temperature is {temp} degrees Fahrenheit with a weather condition of {descr}")
        output = f"In {city_name}\nThe temperature is {temp}" + u"\N{Degree Sign}F\n"+ f"The weather is {descr}"
        return(output)
        #print(f"The Weather Condition is {descr}")
        #print(f"The temperature is {temp}kelvin")
        #print(f"The pressure is {pressure}hPa")
        #print(f"The humidity is {humidity}%")
        #print(f"The speed of wind is {wind}m/s")
    else:
        return("Something went wrong, please try again.")
        # draw.display("Something went wrong, please try again.")