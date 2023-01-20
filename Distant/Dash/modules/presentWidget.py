from dash import html
import dash_bootstrap_components as dbc
import requests
import os

presentCountUrl = os.getenv('PRESENT_URL') if (type(os.getenv('PRESENT_URL')) != type(None)) else "http://gazometre.freeboxos.fr/index.php/user/present-count"
presentCountResponse = requests.get(presentCountUrl, verify=False)
presentCountJson = presentCountResponse.json()
# print(str(presentCountJson[0]['presentUsersCount']))
def PresentWidget():
    presentWidget = dbc.Row(
        [
            dbc.Col(str(presentCountJson[0]['presentUsersCount']), className="present_number", width=5),
            dbc.Col("peoples are present today",
                    className="present_text", width=7)

        ], className="g-0", justify="center", align="center"
    )
    return presentWidget
