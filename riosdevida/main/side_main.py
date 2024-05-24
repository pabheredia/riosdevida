import reflex as rx
from riosdevida.main.Componentes.lista_menu import lista_item


def side_main() -> rx.Component:
    return rx.drawer.root(
        rx.drawer.trigger(rx.button("Deslizar menú")),
        rx.drawer.overlay(z_index="5"),
        rx.drawer.portal(
            rx.drawer.content(
                rx.flex(
                    rx.drawer.close(
                        rx.box(
                            rx.button("Cerrar menú")
                        ),
                        rx.vstack(
                            rx.list(
                                lista_item("Versiculos", "gray"),  # Titulo1
                                rx.list(
                                    rx.link(
                                        lista_item("Filipenses 4:13", "green"),  # Item 1
                                        href="https://www.biblegateway.com/passage"
                                             "/?search=Filipenses%204%3A13&version=RVR1960"
                                    )
                                ),
                                lista_item("Reflexiones", "gray"),  # Titulo2
                                rx.list(
                                    lista_item("Hechos 1:8", "green"),  # Item 1
                                    lista_item("Filipenses 4:13", "green"),  # Item 2
                                ),
                                list_style_type="none",
                            )
                        )
                    ),
                    align_items="start",
                    direction="column",
                ),
                top="auto",
                right="auto",
                height="100%",
                width="20em",
                padding="2em",
                background_color="#FFF"
                # background_color=rx.color("green", 3)
            )
        ),
        direction="left",
    )
