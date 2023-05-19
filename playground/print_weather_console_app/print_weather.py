import requests, argparse
from configparser import ConfigParser


config_file = 'config.ini'
config = ConfigParser()
config.read(config_file)
api_key = config['api_key']['key']


url = "http://api.openweathermap.org/data/2.5/weather?q={}&lang=ru&appid={}"


cities = {
    "kms" : "Komsomolsk-na-amure",
    "habar" : "Khabarovsk"
}


def main():
    parser = argparse.ArgumentParser(description="Print Weather Console App")
    parser.add_argument('city')

    city = parser.parse_args().city

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    try:
        if city in cities:
            resp = requests.get(url.format(cities[city], api_key), headers=headers).json()
        else:
            resp = requests.get(url.format(city, api_key)).json()

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)

    if resp['cod'] == 200:
        temp = float(resp['main']['temp'] - 273.15)
        print(f"Weather: {resp['name']}, {resp['weather'][0]['description']},",
                '+{:.1f}°C'.format(temp if temp > 0 else '{:.1f}°C'.format(temp)))
    else:
        print(resp["message"] or "an error occurred")


if __name__ == '__main__':
    main()
