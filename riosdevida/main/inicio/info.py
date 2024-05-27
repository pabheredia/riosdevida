import reflex as rx


def info_stack() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "Por Pablo Heredia"
        ),
        rx.chakra.highlight(
            "Vivamus sit amet pulvinar urna, commodo auctor lectus. "
            "Morbi egestas turpis sed urna lobortis faucibus. "
            "Phasellus consectetur quis augue ac accumsan. "
            "Proin consectetur purus sit amet ipsum lacinia, "
            "ut malesuada mauris pharetra. Aenean tortor magna, "
            "placerat ac purus nec, volutpat hendrerit sapien. "
            "Donec id quam ac eros maximus aliquet. Etiam efficitur "
            "vitae nibh ut blandit. Nulla eu elit vel risus euismod "
            "pretium. Vivamus auctor venenatis libero rhoncus tristique."
            " Donec non ante ac nulla suscipit vestibulum. Donec ac "
            "ullamcorper dui. Aenean ultricies non erat quis faucibus.",
            query=["Vivamus", "Aenean", "Donec"],
            styles={
                "px": "2",
                "py": "1",
                "rounded": "full",
                "bg": "grey",
            },
        ),
        rx.avatar(
            src="/nomelaton.jpg",
            size="9",
            fallback="PH"
        ),
        width="100%",
        height="auto",
        align="center",
        justify="center"
    )
