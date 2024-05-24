import reflex as rx


def lista_item(text: str, color: str) -> rx.Component:
    return rx.list.item(
                    rx.icon(
                        "square-chevron-right",
                        color=color),
                    text
                )
