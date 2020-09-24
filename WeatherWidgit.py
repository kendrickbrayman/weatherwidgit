import requests as rq
import os
import json

def kelvin2Faren(num):
    return round(((num - 273.15) * 9 / 5) + 32, 1)

class Weather():

    def __init__(self,lat,long):
        self.lat = float(lat)
        self.long = float(long)

    def get(self):
        #lat = 34.026953
        #long = -118.413970
        WeatherKEY = os.environ['APIKEY']

        try:
            weatherData = rq.get(
                'https://api.openweathermap.org/data/2.5/onecall?exclude=current,minutely,hourly,alert',
                params={'lat': self.lat, 'lon': self.long, 'appid': WeatherKEY}).json()

            test = weatherData['test1234'][1][6]

            # convert dt to datetime and find the next weekend to determine how good it is for golf conditions

            outputText = 'The temperature tomorrow should be ' + str(nextDay["feels_like"]['day']) + u"\N{DEGREE SIGN}" + 'F'

            return "outputText"

        except Exception as e:
            return str(e)




