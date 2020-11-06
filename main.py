import get_weather
import forecast_weather

filename = 'weather.json'
url = 'http://t.weather.itboy.net/api/weather/city/101020100'
get_weather.get_weather_json(filename, url)
forecast_weather.forecast(filename)