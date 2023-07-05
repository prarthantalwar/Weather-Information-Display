import requests

def get_weather_info(city, country):
    access_key = 'YOUR-API-KEY'
    url = 'http://api.weatherstack.com/current'

    params = {
        'access_key': access_key,
        'query': f'{city}, {country}'
    }

    try:
        api_result = requests.get(url, params)
        api_response = api_result.json()
        return api_response
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        return None
    except KeyError:
        print("Invalid API response")
        return None

def print_weather_info(api_response):
    if api_response:
        location = api_response['location']
        current = api_response['current']

        print(f"\n\n\nWeather information for {location['name']}, {location['country']}\n")
        print("Region:", location['region'])
        print("Local Time:", location['localtime'])
        print("\n-----------------------------\n")
        print("Current Temperature:", current['temperature'], "°C")
        print("Weather Description:", current['weather_descriptions'][0])
        print("Feels Like:", current['feelslike'], "°C")
        print("Wind Speed:", current['wind_speed'], "km/h")
        print("Wind Direction:", current['wind_dir'])
        print("Pressure:", current['pressure'], "mb")
        print("Precipitation:", current['precip'], "mm")
        print("Humidity:", current['humidity'], "%")
        print("Cloud Cover:", current['cloudcover'], "%")
        print("UV Index:", current['uv_index'])
        print("Visibility:", current['visibility'], "km")
        print("Is it daytime?", current['is_day'])
    else:
        print("Unable to fetch weather information.")

# Get user input for the city and country
city = input("Enter a city name: ")
country = input("Enter the country: ")

# Retrieve weather information
api_response = get_weather_info(city, country)

# Print the weather information
print_weather_info(api_response)
