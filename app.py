from flask import Flask,request
from WeatherWidgit import Weather


app = Flask(__name__)


@app.route('/weather', methods=['GET','POST'])
def webhook():
    if 'lat' and 'long' in request.args:
        lat = request.args['lat']
        long = request.args['long']
        weatherString = Weather(lat,long)
    return weatherString,400

if __name__ == '__main__':
    app.run()

