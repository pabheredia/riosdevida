import reflex as rx


def inicio() -> rx.Component:
    return rx.flex(
        rx.heading(
            "Rios de vida",
            size="9",
            justify="center"
        ),
        rx.heading(
            "Neque porro quisquam est qui dolorem ipsum "
            "quia dolor sit amet, consectetur, adipisci velit...",
            size="6"
        ),
        rx.divider(),
        rx.text(
            "Vivamus sit amet pulvinar urna, commodo auctor lectus. Morbi egestas "
            "turpis sed urna lobortis faucibus. Phasellus consectetur quis augue ac accumsan. "
            "Proin consectetur purus sit amet ipsum lacinia, ut malesuada mauris pharetra. "
            "Aenean tortor magna, placerat ac purus nec, volutpat hendrerit sapien. "
            "Donec id quam ac eros maximus aliquet. Etiam efficitur vitae nibh ut blandit. "
            "Nulla eu elit vel risus euismod pretium. Vivamus auctor venenatis libero rhoncus tristique. "
            "Donec non ante ac nulla suscipit vestibulum. Donec ac ullamcorper dui. "
            "Aenean ultricies non erat quis faucibus."
            "",
            size="6"
        ),
        rx.text(
            "Curabitur semper, ipsum vitae imperdiet tempus, libero est pretium turpis, "
            "eu faucibus velit dolor sed neque. Ut nunc lacus, iaculis vitae justo consectetur, "
            "bibendum euismod nulla. Aenean velit sapien, pharetra et vulputate maximus, "
            "vulputate ut ligula. Ut gravida massa et volutpat tincidunt. Suspendisse viverra lorem a "
            "placerat scelerisque. Nulla sit amet pulvinar est. Lorem ipsum dolor sit amet, consectetur "
            "adipiscing elit. Sed in mi eu mi eleifend hendrerit at vel nunc."
            ""
            "",
            size="6"
        ),
        rx.text(
            "Sed justo justo, pretium et quam a, tincidunt maximus nisl. Donec tristique ex quis "
            "lectus imperdiet, vitae dapibus diam aliquam. Duis eu augue "
            "scelerisque, aliquet neque ut, fringilla libero. Fusce cursus"
            " egestas leo, vel volutpat tellus bibendum ac. Pellentesque at suscipit mi. "
            "Donec condimentum finibus tempor. Quisque porttitor nunc lorem, ac vestibulum "
            "magna varius vitae. In vitae turpis vel ante eleifend malesuada. Curabitur sed"
            " accumsan velit. Donec facilisis sapien leo, in ullamcorper orci congue at. "
            "Donec ut mi sem. Orci varius natoque penatibus et magnis dis parturient montes, "
            "nascetur ridiculus mus. Vivamus ut imperdiet tellus. Proin pretium, nibh quis "
            "vulputate ultrices, ante nisl faucibus quam, id malesuada lectus augue vitae nibh."
            " Nunc fermentum nulla non magna fermentum, sit amet vulputate elit pharetra. "
            "In maximus, ex quis aliquam scelerisque, justo nibh fermentum sem, a "
            "placerat sapien metus eu leo.",
            size="6",
            high_contrast=True
        ),
        padding="1em",
        spacing="4",
        direction="column"
    )
