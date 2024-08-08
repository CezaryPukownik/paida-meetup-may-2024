# PAIDA 2024 DEMO INSTRUCTIONS

### Setup
1. Create a new folder called `paida-demo`
2. Setup venv `uv .venv`.
3. Install requirements. 
4. Make sure Docker Desktop is running.
5. Delete all old docker containers.
6. DROP all clickhouse tables.
7. Make sure port 9000 and 3000 is not accupied.

    > netstat -tulpn | grep ":9000"
    > kill -9 [pid]

8. Setup OpenWeather API Key as `API_KEY` environment variable.

## General ChatGPT Formula:
[PERSONA] + [TASK] + [CONTEXT] + [CONSTRAINTS]

### Create Infrastructure
#### Prompt 1: Create Infrastructure
You are a Data Engineer. 
Create a docker application that will contain latest Clickhouse and Grafana. 
Respond with markdown codeblock and nothing else.

1. Create a `docker-compose.yml` file, copy and paste AI Buddy response 
2. Create a tmux tab and run `docker compose up`
3. Open browser at `localhost:3000` to see if Grafana is running. `admin: admin`
4. Login to clickhouse to see if clickhouse is running `clickhouse-client`


#### Prompt 2: Create API Clinet
You are professional Python Developer. 
Write a production ready python code that will use OpenWheather API 
to fetch hourly wheather forecast in Poznań, Poland and save it to Clickhouse.
OpenWeather API Key is stored under `API_KEY` environment variable.
Respond with markdown codeblock and nothing else.

1. Create a `openweather.py` file, copy and paste AI Buddy response.
2. Make sure that this is connecting to localhost.

##### Subprompt: Generate a requirements.txt for the project.
Generate a requirements.txt for the project.

#### Prompt 3: Create Clickhouse Table
You are a experianced Database Administrator.
Write a SQL Create Table DDL Statement that will match data from OpenWeather.
Respond with markdown codeblock and nothing else.


#### Prompt 4: Write a SQL Transformations
You are a Senior Analytics Engineer.
Create a view in Clickhouse that will calculate min, max and avg temperature for each day based on previously created table.
Respond with markdown codeblock and nothing else.


#### Prompt 5: Create a Grafana Dashboard.
You are a experianced BI Developer. Create a grafana dashboard with two line charts.
First graph on the left is representing daily summary. Second one is respresenting hourly data.
Return a SQL Queries that will be used to create those charts.
Respond with markdown codeblock and nothing else.


