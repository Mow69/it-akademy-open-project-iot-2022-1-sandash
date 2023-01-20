from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


def DateWidget():
    dateWidget = html.Div(
        [
            html.H2(["Tuesday", html.Br(), "January 4, 2022 "]),
            html.Div(id='circle_clock'),
            html.Div(dbc.Row(
                [
                    dbc.Col(DashIconify(
                        icon="bi:globe2",
                        color="rgba(255, 255, 255, 0.46)",
                        width=57,
                    ),
                        width={"size": 2, "offset": 1}),
                    dbc.Col(
                        [html.P("(UTC+1) 14:40:32",
                                className="utc_clock"), html.P("LONDON")
                         ])
                ], className="g-0", justify="center"), className="date_footer")
        ]
    )
    return dateWidget
