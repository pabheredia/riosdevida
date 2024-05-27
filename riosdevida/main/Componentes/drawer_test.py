import reflex as rx
from riosdevida.main.Componentes.lista_menu import lista_item


def drawer() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(
            rx.button(
                rx.icon(tag="menu"),
                "Índice",
                radius="full",
                color_scheme="ruby"
            )
        ),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.flex(
                    rx.drawer.close(
                        rx.box(
                            rx.button(
                                rx.icon(tag="x"),
                                "Cerrar",
                                radius="full"
                            )
                        )
                    ),
                    rx.vstack(
                        rx.heading("->Indice"),
                        rx.vstack(
                            rx.list(
                                rx.link(
                                    lista_item("Filipenses 4:13", "green"),  # Item 1
                                    href="https://www.biblegateway.com/passage"
                                         "/?search=Filipenses%204%3A13&version=RVR1960"
                                ),
                                rx.link(
                                    lista_item("Hechos 1:8", "green"),  # Item 1
                                    href="https://www.biblegateway.com/passage"
                                         "/?search=Filipenses%204%3A13&version=RVR1960"
                                ),
                                list_style_type="none",
                            )
                        ),
                        align_items="start",
                        direction="column"
                    ),
                    top="auto",
                    right="auto",
                    height="100%",
                    width="20em",
                    padding="2em",
                    # background_color="#FFF",
                    background_color=rx.color("ruby", 3)
                )
            ),
            direction="left"
        )
    )
