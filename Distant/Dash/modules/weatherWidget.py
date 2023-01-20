import dash
from dash_iconify import DashIconify
from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc
import requests
import json
import pandas as pd

url = "http://api.openweathermap.org/data/2.5/forecast?q=Lyon&appid=457da71e006d11b859b1ae7faea29650&units=metric"
request_weather = requests.get(url).json()
json_dict = json.dumps(request_weather['list'][0]['main'])
data_temp_0_f = request_weather['list'][0]['main']['temp']
data_temp_0_int = int(data_temp_0_f)
data_temp_0 = str(data_temp_0_int) + "°"
hourly_data_0 = request_weather['list'][0]["dt_txt"]
weather_description = request_weather['list'][1]["weather"][0]["description"]
data_temp_min_f = request_weather['list'][0]['main']['temp_min']
data_temp_min1_int = int(data_temp_min_f)
data_temp_min1 = str(data_temp_min1_int) + "°"
hourly_data_1 = request_weather['list'][0]["dt_txt"]
data_temp_max_f = request_weather['list'][0]['main']['temp_max']
data_temp_max1_int = int(data_temp_max_f)
data_temp_max1 = str(data_temp_max1_int) + "°"
hourly_data_2 = request_weather['list'][0]["dt_txt"]

data_temp_min2_f = request_weather['list'][6]['main']['temp_min']
data_temp_min2_int = int(data_temp_min2_f)
data_temp_min2 = str(data_temp_min2_int) + "°"
hourly_data_1 = request_weather['list'][8]["dt_txt"]
data_temp_max_f = request_weather['list'][8]['main']['temp_max']
data_temp_max2_int = int(data_temp_max_f)
data_temp_max2 = str(data_temp_max2_int) + "°"
hourly_data_3 = request_weather['list'][8]["dt_txt"]
temp1 = pd.Timestamp(request_weather['list'][0]["dt_txt"])
daily1 = temp1.day_name()
temp2 = pd.Timestamp(request_weather['list'][8]["dt_txt"])
daily2 = temp2.day_name()
icon = 'http://openweathermap.org/img/wn/10n@2x.png'
icon1 = request_weather['list'][0]['weather'][0]['icon']


def WeatherWidget():

    weatherWidget = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(DashIconify(
                        icon="bi:cloud-sun",
                        color="rgba(255, 255, 255, 1)",
                        width=148,
                    ),
                        width=7,
                        style={'textAlign': 'center'}),
                    dbc.Col(html.P(data_temp_0, className="main_temperature"), width=5
                            )
                ], className="g-0", justify="center"),
            html.Div(html.P(weather_description), className="weather_legend"),
            dbc.Row(
                [
                    dbc.Col([
                        html.H4(daily1), dbc.Row([
                            dbc.Col(DashIconify(
                                icon="bi:clouds",
                                color="rgba(255, 255, 255, 1)",
                                width=85,
                            ),
                                width=6),
                            dbc.Col([
                                html.P(data_temp_min1),
                                html.Hr(),
                                html.P(data_temp_max1),
                            ], width=4)
                        ], justify="center")
                    ], width=6),
                    dbc.Col([
                        html.H4(daily2),
                        dbc.Row([
                            dbc.Col(DashIconify(
                                icon="bi:sun",
                                color="rgba(255, 255, 255, 1)",
                                width=85,
                            ),
                                width=6),
                            dbc.Col([
                                html.P(data_temp_min2),
                                html.Hr(),
                                html.P(data_temp_max2),
                            ], width=4)
                        ], justify="center")
                    ], width=6)
                ], justify="center", id="forecast_days", className="g-0"),

        ]
    )

    return weatherWidget
