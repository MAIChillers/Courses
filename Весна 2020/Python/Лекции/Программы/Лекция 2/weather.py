"""Вывод погоды в терминал.

Для запуска передать в качестве аргумента название города
Документация по API https://openweathermap.org/current
"""
import requests
import json
import sys


def get_weather(city):
    """Получение погоды в формате JSON."""
    # Нужно полуить новый ключ на https://home.openweathermap.org/api_keys
    # Возможно потребуется включить VPN
    # WARNING: Данный ключ больше не работает
    TOKEN = "94654af73b349f2bc72db391d9d2cfda"
    url = "http://api.openweathermap.org/data/2.5/weather?"
    url = url + "q={}&appid={}&units=metric".format(city, TOKEN)
    try:
        weather = requests.get(url)
    except any:
        return None
    if not weather.status_code == 200:
        return None
    weather_json = json.loads(weather.text)
    return weather_json


weather_json = get_weather(sys.argv[1])

if weather_json is None:
    print("Город введен неправильно или произошла другая ошибка")
else:
    print("Погода в {}".format(weather_json["name"]))
    print("Температура: {}C, ощущается как {}".format(weather_json["main"]["temp"],
          weather_json["main"]["feels_like"]))
    print("Ветер: {} м/с, направление {}".format(weather_json["wind"]["speed"],
          weather_json["wind"]["deg"]))
