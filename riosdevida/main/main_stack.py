import reflex as rx
from riosdevida.main.top_nav_bar import top_nav
from riosdevida.main.side_main import side_main
from riosdevida.main.footer import footer


def main_stack(section: rx.Component) -> rx.Component:
    return rx.vstack(
        top_nav(),
        rx.hstack(
            side_main(),
            rx.scroll_area(
                section,
                type="auto",
                scrollbars="vertical",
                height="50em",
                width="100%"
            )
        ),
        footer(),
        width="100%",
        height="auto",
        align="center",
        justify="center",

    )
