"""Der Kreis – die einzige Form, die kein Polygon ist."""
from math import pi
from typing import Final, override

from form import Form
from punkt import Punkt


class Kreis(Form):
    """Ein Kreis, festgelegt durch Mittelpunkt und Radius.

    >>> k = Kreis(Punkt(2, 3), 5)
    >>> k
    Kreis(Punkt(2, 3), 5)
    >>> round(k.flaeche(), 4)
    78.5398
    >>> round(k.umfang(), 4)
    31.4159
    >>> k.verschoben(1, 1)
    Kreis(Punkt(3, 4), 5)
    >>> k                      # das Original bleibt unveraendert
    Kreis(Punkt(2, 3), 5)
    >>> k.kennwerte()["radius"]
    5
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

    def verschoben(self, dx: int | float, dy: int | float) -> "Kreis":
        return Kreis(self.mittelpunkt.verschoben(dx, dy), self.radius)

    def kennwerte(self) -> dict:
        """Erweitert die geerbten Kennwerte – super() liefert die Basis."""
        return super().kennwerte() | {"mittelpunkt": str(self.mittelpunkt),
                                      "radius": self.radius}
