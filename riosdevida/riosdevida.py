"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from riosdevida.main.Componentes.link_button import link_button1
from riosdevida.main.main_stack import main_stack
from riosdevida.main.inicio.galeria import galeria_stack
from riosdevida.main.inicio.inicio import inicio
from riosdevida.main.inicio.info import info_stack
from riosdevida.main.inicio.links import links_stack
from riosdevida.main.versiculos.hechos1_8 import hechos1_8
from riosdevida.main.versiculos.hechos1_8 import mateo


def index() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.image(
                src="/logo.JPG",
                width="100px",
                height="auto",
                border_radius="15px 50px",
                border="2px solid #555",
            ),
            href="/"
        ),
        rx.hstack(
            link_button1("Entrar!", "/main", "tween"),
            link_button1("!", "/about", "ease-in"),
        ),
        align="center",
        justify="center",
        padding="15em"
    )


def main() -> rx.Component:
    return main_stack(inicio())


def galeria() -> rx.Component():
    return main_stack(galeria_stack())


def informacion() -> rx.Component:
    return main_stack(info_stack())


def links() -> rx.Component:
    return main_stack(links_stack())


def hechos() -> rx.Component:
    return main_stack(hechos1_8())


def mateo7() -> rx.Component:
    return main_stack(mateo())


app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="teal"
    )
)
app.add_page(index)
app.add_page(main)
app.add_page(galeria)
app.add_page(informacion, route="/info")
app.add_page(links(), route="/links")
app.add_page(hechos(), route="/hechos1_8")
app.add_page(mateo7(), route="/mateo71314")
