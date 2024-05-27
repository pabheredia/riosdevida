import reflex as rx


def side_main() -> rx.Component:
    return rx.vstack(
        rx.scroll_area(
            rx.chakra.accordion(  # Llamo al componente accordion
                rx.chakra.accordion_item(  # LLamo a un item del accordion
                    rx.chakra.accordion_button(  # agrego un botón al item
                        rx.icon(tag="home", stroke_width=1, size=15),  # inserto un icono de home
                        rx.heading(" Inicio")  # Le coloco un texto heading
                    ),
                    rx.chakra.accordion_panel(  # LLamo al panel del acordeón
                        rx.link(  # Agrego un componente link de reflex
                            rx.icon(tag="home", stroke_width=1, size=15),
                            href="/main"
                        )
                    ),
                    rx.chakra.accordion_panel(  # LLamo al panel del acordeón
                        rx.link(  # Agrego un componente link de reflex
                            rx.text(  # lo que estará enlazado será el texto
                                " Galería"
                            ),
                            href="/galeria"
                        )
                    ),
                    rx.chakra.accordion_panel(  # LLamo al panel del acordeón
                        rx.link(  # Agrego un componente link de reflex
                            rx.text(  # lo que estará enlazado será el texto
                                "Informacion"
                            ),
                            href="/info"
                        )
                    ),
                    rx.chakra.accordion_panel(  # LLamo al panel del acordeón
                        rx.link(  # Agrego un componente link de reflex
                            rx.text(  # lo que estará enlazado será el texto
                                "Links"
                            ),
                            href="/links"
                        )
                    )
                ),
                rx.chakra.accordion_item(
                    rx.chakra.accordion_button(
                        rx.icon(tag="images", stroke_width=1, size=15),
                        rx.heading("Versiculos"),
                        rx.chakra.accordion_icon(),
                    ),
                    rx.chakra.accordion_panel(
                        rx.link(
                            rx.text(
                                "Hechos 1:8"
                            ),
                            href="/hechos1_8"
                        )
                    ),
                    rx.chakra.accordion_panel(
                        rx.link(
                            rx.text(
                                "Mateo 7:13-14"
                            ),
                            href="/mateo71314"
                        )
                    )
                ),
                allow_toggle=True,
                default_index=[0],
                bg="black",
                color="white",
                width="100%",
            ),
            type="auto",
            scrollbars="vertical",
            height="100%"
        )
    )
