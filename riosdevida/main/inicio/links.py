import reflex as rx
from riosdevida.main.Componentes.link_button import link_button1


def links_stack() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Pagina de links"
        ),
        link_button1("Instagram", "instagram.com/nomelaton", "tween")
    )
