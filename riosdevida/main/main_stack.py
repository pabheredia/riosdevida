import reflex as rx
from riosdevida.main.top_nav_bar import top_nav
# from riosdevida.main.side_main import side_main
from riosdevida.main.Componentes.head_main import posts_esquema
from riosdevida.main.Componentes.drawer_test import drawer
from riosdevida.main.Componentes.posts_texts import Textos


def main_stack() -> rx.Component:
    return rx.vstack(
        top_nav(),
        rx.hstack(
            rx.vstack(
                drawer(),
                align="center",
                justify="center",
                padding="1em"
            ),
            rx.vstack(
                posts_esquema(Textos.hechos_1_8, Textos.hechos_1_8_refl, "/hechos_1_8.jpg", "Hechos 1:8"),
                posts_esquema(Textos.mateo_7_1314, Textos.mateo_7_1314_refl, "/mateo_7_1314.jpg", "Mateo 7:13-14"),
                padding="1em"
            )
        ),
        width="100%",
        height="auto",
    )
