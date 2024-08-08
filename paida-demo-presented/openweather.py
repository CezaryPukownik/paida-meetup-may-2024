import os
import requests
import logging
from datetime import datetime
import clickhouse_driver

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Constants
API_KEY = os.getenv('API_KEY')
CITY_NAME = "Poznan,PL"
OPENWEATHER_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"
CLICKHOUSE_HOST = "localhost"


def get_weather(api_key, city_name):
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(OPENWEATHER_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()['list']


def save_to_clickhouse(host, data):
    # Establish a connection to the ClickHouse server
    connection = clickhouse_driver.Client(host)

    # Create the database and table if not exist
    create_db_query = "CREATE DATABASE IF NOT EXISTS weather"
    create_table_query = """
    CREATE TABLE IF NOT EXISTS weather.forecast (
        city String,
        datetime DateTime,
        temperature Float32,
        feels_like Float32,
        pressure UInt16,
        humidity UInt8
    ) ENGINE = MergeTree()
    ORDER BY datetime
    """

    connection.execute(create_db_query)
    connection.execute(create_table_query)

    # Prepare data for insertion
    insert_query = "INSERT INTO weather.forecast (city, datetime, temperature, feels_like, pressure, humidity) VALUES"
    insert_data = [(CITY_NAME, datetime.fromtimestamp(item['dt']),
                    item['main']['temp'], item['main']['feels_like'],
                    item['main']['pressure'], item['main']['humidity'])
                   for item in data]

    # Insert data into the ClickHouse table
    connection.execute(insert_query, insert_data)
    logger.info(f"Inserted {len(insert_data)} rows into ClickHouse")


def main():
    logger.info("Fetching weather data...")
    try:
        weather_data = get_weather(API_KEY, CITY_NAME)
        logger.info("Saving data to ClickHouse...")
        save_to_clickhouse(CLICKHOUSE_HOST, weather_data)
        logger.info("Data saved successfully.")
    except requests.RequestException as e:
        logger.error(f"Error fetching data from OpenWeather API: {e}")
    except clickhouse_driver.errors.Error as e:
        logger.error(f"Error saving data to ClickHouse: {e}")


if __name__ == "__main__":
    main()
