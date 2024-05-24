import reflex as rx


def posts_esquema(versiculo: str, reflexion: str, source: str, titulo: str) -> rx.Component:
    return rx.vstack(
        rx.heading(titulo),
        rx.image(src=source),
        rx.text.strong(
            versiculo,
            weight="bold",
            as_="div",
            align="center"
        ),
        rx.text(
            reflexion,
            align="left"
        ),
        direction="column",
        spacing="3",
        width="100%",
        align="center",
        justify="center"
    )
