from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify
import requests
import os

dayNameResponse = requests.post('https://nameday.abalin.net/today?country=France', verify=False)
dayNameJson = dayNameResponse.json()

calendarUrl = os.getenv('CALENDAR_URL') if (type(os.getenv('CALENDAR_URL')) != type(None)) else "http://gazometre.freeboxos.fr/index.php/task/today"

calendarResponse = requests.get(calendarUrl, verify=False)
calendarJson = calendarResponse.json()


def PlanningWidget():
    planningWidget = dbc.Row(
        [
            dbc.Col(html.Div([
                html.H2("TODAY’S PLANNING"),
                dbc.Row(
                    [
                        dbc.Col(DashIconify(
                            icon="vs:party",
                            color="rgba(255, 255, 255, 1)",
                            width=59,
                        ),
                            width=2,
                            style={'textAlign': 'center'}),
                        dbc.Col([html.H3("SAINT " + dayNameJson['data']['namedays']['fr'] + "’S DAY"), html.H4("HAPPY BIRTHDAY GORDON RAMSEY !",
                                                                        className="birthday_plan")
                                 ], width="auto"),
                    ], justify="center", className="g-0", id="head_planning_footer")
            ],
                className='head_planning_widget'), width=12),
            dbc.Col(html.Div(dbc.Row([
                dbc.Col((calendarJson[0]['start'] + '-' + calendarJson[0]['end']) if 0 < len(
                    calendarJson) else '', width=3, className="event_hours"),
                dbc.Col(html.Div("", className="splitter"), width="auto"),
                dbc.Col(calendarJson[0]['title'] if 0 < len(calendarJson) else '',
                        className="event_desc", width="auto"),
            ], justify="start", className="g-0"), className='content_planning_widget'),
                width=12),
            dbc.Col(html.Div(dbc.Row([
                dbc.Col((calendarJson[1]['start'] + '-' + calendarJson[1]['end']) if 1 < len(
                    calendarJson) else '', width=3, className="event_hours"),
                dbc.Col(html.Div("", className="splitter"), width="auto"),
                dbc.Col(calendarJson[1]['title'] if 1 < len(calendarJson) else '',
                        className="event_desc", width="auto")
            ], justify="start", className="g-0"), className='content_planning_widget'),
                width=12),
            dbc.Col(html.Div(dbc.Row([
                dbc.Col((calendarJson[2]['start'] + '-' + calendarJson[2]['end']) if 2 < len(
                    calendarJson) else '', width=3, className="event_hours"),
                dbc.Col(html.Div("", className="splitter"), width="auto"),
                dbc.Col(calendarJson[2]['title'] if 2 < len(calendarJson) else '',
                        className="event_desc", width="auto")
            ], justify="start", className="g-0"), className='content_planning_widget'),
                width=12),
        ], className="g-3"
    )
    return planningWidget
