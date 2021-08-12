import requests
from requests.models import HTTPError
from systemFunctions import speak, draw_text

def weather_data(query):
    res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=8de0c1d186a15c6c44a58c73ca31e976&units=metric');
    # Check if city exists
    if (res.json()['cod'] == '404') :
          raise HTTPError
    return res.json();

def print_weather(city, result):
    # Print weather
    w1 = ("{}'s temperature: {}°C ".format(city, result['main']['temp']))
    w2 = ("Wind speed: {} meters per second".format(result['wind']['speed']))
    w3 = ("Weather description: {}".format(result['weather'][0]['description']))
    w = w1 + w2 + w3 

    print("{}'s temperature: {}°C ".format(city,result['main']['temp']))
    print("Wind speed: {} m/s".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))
    draw_text(str(result['weather'][0]['main']))
    speak(w)

def weather():
  city = "Toronto"
  
  try :
    query='q='+city;
    w_data=weather_data(query);
    # print(w_data)
    print_weather(city, w_data)
    print()
    
  except HTTPError :
    print('City name not found...')
