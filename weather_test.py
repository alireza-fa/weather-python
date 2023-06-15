import requests
from datetime import datetime

URL = 'http://api.openweathermap.org/data/2.5/weather?q={}' \
          '&appid=b93e093a69b8c26a0daebcbb68e542df&units=metric'


def by_city():
    city = input('Enter your city : ')
    res = requests.get(URL.format(city))
    if res.status_code == 200:
        data = res.json()
        return show_data(data)
    raise ValueError


def show_data(data):
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']
    timestamps = data['dt']
    datetime_now = datetime.fromtimestamp(timestamps)

    print()
    print('Temperature : {} degree celcius'.format(temp))
    print('Wind Speed : {} m/s'.format(wind_speed))
    print('Latitude : {}'.format(latitude))
    print('Longitude : {}'.format(longitude))
    print('Description : {}'.format(description))
    print(f'Datetime: {datetime_now}')


if __name__ == '__main__':
    by_city()
