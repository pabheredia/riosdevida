import reflex as rx
from reflex_motion import motion


class PropValues:
    BIG_BUTTON = {

    }


def link_button1(text: str, url: str, transition_type: str) -> rx.Component:
    return rx.link(
            motion(
                rx.button(
                    text,
                    width="100%",
                    variant="outline",
                    color_scheme="ruby",
                    high_contrast=True,
                    radius="full"
                ),
                while_hover={"scale": 1.2},
                while_tap={"scale": 0.9},
                transition={
                    "type": transition_type,  # tween, ease, linear, ease-in, ease-out
                    "stiffness": 400,
                    "damping": 17}
            ),
            href=url,
            # is_external=True
        )


def link_button2(text: str, tag: str, url: str, transition_type: str) -> rx.Component:
    return rx.link(
            motion(
                rx.button(
                    rx.icon(tag=tag),
                    text,
                    width="100%",
                    variant="outline",
                    color_scheme="ruby",
                    high_contrast=True,
                    radius="full"
                ),
                while_hover={"scale": 1.2},
                while_tap={"scale": 0.9},
                transition={
                    "type": transition_type,  # tween, ease, linear, ease-in, ease-out
                    "stiffness": 400,
                    "damping": 17}
            ),
            href=url,
            # is_external=True
        )
