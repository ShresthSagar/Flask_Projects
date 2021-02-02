import requests
import configparser
from flask import Flask, render_template, request
app = Flask(__name__)


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    # print(config.sections())
    return config['openweathermap']['api_key']


def get_weather_result(city_name, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city_name, api_key)
    print(api_url)
    raw_json = requests.get(api_url)
    return raw_json.json()


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/results', methods=['POST'])
def render_results():
    city_name = request.form['city']
    data = get_weather_result(city_name, get_api_key())
    description = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    pressure = data["main"]["pressure"]
    humidity = data["main"]["humidity"]
    visibility = data["visibility"]
    wind_speed = data["wind"]["speed"]
    return render_template('results.html', temp=temp, feels_like=feels_like,
                           humidity=humidity, city_name=city_name, visibility=visibility,
                           pressure=pressure, description=description, wind_speed=wind_speed
                           )


print(get_weather_result("GHAZIABAD", get_api_key()))

if __name__ == '__main__':
    app.run(debug=True)
