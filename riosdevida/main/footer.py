import reflex as rx


def footer() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.text(
                "Creative Common. by nomelaton"
            ),
            href="instagram.com/nomelaton",
            is_external=True
        ),
        rx.link(
            rx.avatar(
                src="https://banner2.cleanpng.com/20180711"
                    "/iqy/kisspng-github-computer-icons-github-"
                    "logo-5b459a3d238b60.4061479515312881251456.jpg",
                variant="soft",
                size="3",
                color_scheme="ruby",
                radius="large",
                fallback="NM"
            ),
            href="https://github.com/pabheredia",
            is_external=True
        ),
        align="center",
        justify="center"
    )
