import reflex as rx
from riosdevida.main.Componentes.link_button import link_button1
from riosdevida.main.Componentes.link_button import link_button2


def top_nav() -> rx.Component:
    return rx.hstack(
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
        rx.spacer(),
        link_button2("IG", "instagram", "https://www.instagram.com/riosdevidamonteros/", "ease-in"),
        link_button1("INFO", "/info", "ease-in"),
        link_button2("", "home", "/", "ease-out"),
        background="linear-gradient(90deg, rgba(29,20,0,1) 22%, rgba(255,56,56,1) 100%)",
        width="100%",
        justify="center",
        align="center",
        padding="1em"
    )
