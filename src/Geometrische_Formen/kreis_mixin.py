"""Der Kreis – die einzige Form, die kein Polygon ist."""
from math import pi
from typing import Final, override

from form import Form
from punkt import Punkt
from mixins import VergleichMixin, JsonMixin


class Kreis(VergleichMixin, JsonMixin, Form):
    """
    Ein Kreis, festgelegt durch Mittelpunkt und Radius.
    """
    def __init__(self, mittelpunkt: Punkt, radius: int | float) -> None:
        if radius <= 0:
            raise ValueError(f"radius={radius} muss positiv sein.")
        self.mittelpunkt: Final[Punkt] = mittelpunkt
        self.radius: Final[int | float] = radius


    def __repr__(self) -> str:
        return f"Kreis({self.mittelpunkt!r}, {self.radius})"


    @override
    def flaeche(self) -> float:
        return pi * self.radius ** 2


    @override
    def umfang(self) -> float:
        return 2 * pi * self.radius


    def to_dict(self):
        """Konvertiert das Kreis-Objekt in ein Dictionary."""
        return {
            "mittelpunkt": {
                "x": self.mittelpunkt.x,
                "y": self.mittelpunkt.y,
            },
            "radius": self.radius,
        }