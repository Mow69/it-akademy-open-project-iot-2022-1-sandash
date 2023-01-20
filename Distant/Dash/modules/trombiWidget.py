from dash import html
import dash_bootstrap_components as dbc


def TrombiWidget():
    trombiWidget = html.Div(
        [
            html.Img(src="/assets/img/david_kang2.jpg",
                     className="background_photo"),
            html.Div(html.Img(src="/assets/img/david_kang2.jpg"),
                     className="profil_photo"),
            html.H3("Daniel Kang"),
            html.H4("Community manager"),
        ],
        id="trombi_wrap",
    )
    # ], style={'backgroundImage': 'url("/assets/img/david_kang2.jpg")', 'backgroundRepeat': 'no-repeat', 'backgroundPosition': 'center', 'backgroundSize': 'cover', 'width': '100%', 'minHeight': '387px', 'borderRadius': '25px'}

    return trombiWidget
