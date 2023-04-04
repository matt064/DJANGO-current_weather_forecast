from django.shortcuts import render
import requests
import datetime
from dotenv import load_dotenv
import os


load_dotenv()


def api_current_weather(request, city):
    "import data about current weather"
    app_key = os.getenv('app_key')
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': app_key, 'units': 'metric',}

    r = requests.get(url=url, params=params)
    res = r.json()

    return res


def select_city(request):
    """import a city"""
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Warszawa'

    return city


def index(request):

    city = select_city(request)

    res = api_current_weather(request, city)

    description = res['weather'][0]['description']
    icon = res['weather'][0]['icon']
    temp = int(res['main']['temp'])
    temp_min = int(res['main']['temp_min'])
    temp_max = int(res['main']['temp_max'])
    humidity = res['main']['humidity']
    pressure = res['main']['pressure']
    wind = int(res['wind']['speed'])

    day = datetime.date.today()

    return render(
        request, 
        'weatherapp/index.html', 
        {'description': description, 'icon': icon, 'temp': temp, 'day': day, 
         'city': city, 'temp_max': temp_max, 'temp_min': temp_min, 'humidity': humidity,
         'pressure': pressure, 'wind': wind}
        )
