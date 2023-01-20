from datetime import date
import dash
from dash import Input, Output, dcc, html
import dash_bootstrap_components as dbc
from modules import presentWidget, infosWidget, planningWidget, dateWidget, weatherWidget, trombiWidget

external_stylesheets = [
    'https://fonts.googleapis.com/css2?family=BenchNine:wght@700&family=Open+Sans:wght@300;700&family=Oswald:wght@500&display=swap',
    dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div(dateWidget.DateWidget(), id='date_widget'), width=4),
        dbc.Col(html.Div(trombiWidget.TrombiWidget(),
                id='trombi_widget'), width=4),
        dbc.Col(html.Div(weatherWidget.WeatherWidget(),
                id='weather_widget'), width=4),
        dbc.Col([
            dbc.Row([
                dbc.Col(html.Div(presentWidget.PresentWidget(),
                        id='present_widget'), width=12),
                dbc.Col(html.Div(infosWidget.InfosWidget(),
                        id='infos_widget'), width=12)
            ], className="g-4")
        ], width=4),
        dbc.Col(html.Div(planningWidget.PlanningWidget(), style={
                'maxHeight': '387px', 'overflow': "hidden"}), width=8)
    ], className="g-4"),
], style={"background": "#E8EBF6", "padding": "20px"})


if __name__ == '__main__':
    app.run_server(debug=True, host='127.0.0.1')
