import reflex as rx


def galeria_stack() -> rx.Component:
    return rx.vstack(
            rx.image(
                src="/hechos_1_8.jpg"
            ),
            rx.spacer(),
            rx.image(
                src="/mateo_7_1314.jpg"
            ),
            padding="1em",
            spacing="4",
            direction="column"
        )
