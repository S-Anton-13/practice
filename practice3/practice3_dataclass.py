import dataclasses


@dataclasses.dataclass
class Product:
    name: str | None = None
    coast: float | None = None

