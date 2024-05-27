import reflex as rx
from riosdevida.main.Componentes.head_main import posts_esquema
from riosdevida.main.Componentes.posts_texts import Textos


def hechos1_8() -> rx.Component:
    return rx.vstack(
        posts_esquema(Textos.hechos_1_8, Textos.hechos_1_8_refl, "/hechos_1_8.jpg", "Hechos 1:8")
    )


def mateo() -> rx.Component:
    return rx.vstack(
        posts_esquema(Textos.mateo_7_1314, Textos.mateo_7_1314_refl, "/mateo_7_1314.jpg", "Mateo 7:13-14")
    )
