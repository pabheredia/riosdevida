"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from riosdevida.main.Componentes.link_button import link_button1
from riosdevida.main.main_stack import main_stack


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
    return main_stack()


app = rx.App()
app.add_page(index)
app.add_page(main)
