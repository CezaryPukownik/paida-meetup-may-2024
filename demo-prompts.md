# PAIDA MAY 2024 DEMO INSTRUCTIONS

## Create Infrastructure

### Prompt 1: Create Infrastructure
You are professional Data Engineer.
Create a docker application that will contain latest Clickhouse and Grafana. 
Respond with markdown codeblock and nothing else.

### Prompt 2: Create an Injestion Script
You are professional Python Developer. 
Write a production ready python code that will use OpenWeather API 
to fetch hourly wheather forecast in Poznań, Poland and save it to Clickhouse.
OpenWeather API Key is stored under `API_KEY` environment variable.
Respond with markdown codeblock and nothing else.

### Prompt 3: Write a SQL Transformations
You are a Senior Analytics Engineer.
Write a SQL Query in Clickhouse that will calculate min, max and avg temperature 
for each day based on previously created table.
Respond with markdown codeblock and nothing else.

### Prompt 4: Schedule execution using Cron
Write a command to schedule execution of `openweather.py` script every day at 9:00.
