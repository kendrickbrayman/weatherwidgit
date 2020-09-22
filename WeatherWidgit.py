import requests as rq
import os
import json


def kelvin2Faren(num):
    return round(((num - 273.15) * 9 / 5) + 32, 1)


lat = 34.026953
long = -118.413970
WeatherKEY = os.environ['APIKEY']

weatherData = rq.get(
    'https://api.openweathermap.org/data/2.5/onecall?exclude=current,minutely,hourly,alert',
    params={'lat': lat, 'lon': long, 'appid': WeatherKEY}).json()

nextDay = weatherData['daily'][1]

# convert dt to datetime and find the next weekend to determine how good it is for golf conditions

outputText = 'The temperature tomorrow should be ' + str(nextDay["feels_like"]['day']) + u"\N{DEGREE SIGN}" + 'F'

jsonOutput = json.loads(json.dump({'text':outputText,'url':"google.com"}))

rq.post('https://widgetweatherudpate.herokuapp.com/',json=jsonOutput)
