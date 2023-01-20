from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


def InfosWidget():
    infosWidget = html.Div(
        [
            dbc.Row([
                dbc.Col(DashIconify(
                    icon="ph:drop-light",
                    color="rgba(255, 255, 255, 1)",
                    width=57,
                ),
                    width=3, style={'textAlign': 'center'}),
                dbc.Col(
                    html.H3("18% HUMIDITY"), width=8),
                dbc.Col(DashIconify(
                    icon="bi:thermometer-half",
                    color="rgba(255, 255, 255, 1)",
                    width=53,
                ),
                    width=3, style={'textAlign': 'center'}),
                dbc.Col(
                    html.H3("20° inside the building"), width=8)
            ], className="g-1", justify="center", align="center")
        ]
    )
    return infosWidget
