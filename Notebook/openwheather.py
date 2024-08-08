import os
import requests
from typing import Dict, Any

API_KEY: str = os.environ['API_KEY']
BASE_URL: str = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name: str, api_key: str) -> Dict[str, Any]:
    """
    Get the current weather data for the specified city using the OpenWeather API.
    
    :param city_name: Name of the city to get the weather for.
    :param api_key: Your OpenWeather API key.
    :return: A dictionary representation of the JSON response from the API.
    """
    params: Dict[str, str] = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Get the temperature in Celsius
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
    return response.json()


def main():
    """
    Main function to repeatedly fetch and print the current weather data for Poznań, Poland.
    """
    try:
        weather_data = get_weather("Poznań,PL", API_KEY)
        # TODO: Process the `weather_data` as needed or store it for later analysis.
        print(weather_data)  # Placeholder for demonstration
    except requests.HTTPError as e:
        print(f"HTTPError: {e}")
    except requests.RequestException as e:
        print(f"RequestException: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    

if __name__ == "__main__":
    main()
