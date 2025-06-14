# weather_dashboard.py
import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        print(f"Error: {data.get('message')}")
        return

    print("\n--- Weather Dashboard ---")
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Get weather information for a city.')
    parser.add_argument('city', help='City name')
    parser.add_argument('--apikey', help='Your OpenWeatherMap API key', required=True)
    args = parser.parse_args()
    get_weather(args.city, args.apikey)
