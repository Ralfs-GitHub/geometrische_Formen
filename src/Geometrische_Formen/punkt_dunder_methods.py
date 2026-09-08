from math import isfinite, sqrt
from types import NotImplementedType
from typing import Final


class Punkt:
    """
    Ein Punkt in der zweidimensionalen Ebene.
    """

    def __init__(self, x: int | float, y: int | float) -> None:
        """
        Erzeugt einen Punkt und setzt seine Koordinaten.

        :param x: die x-Koordinate des Punktes
        :param y: die y-Koordinate des Punktes
        :raises ValueError: wenn eine Koordinate nicht endlich ist
        """
        if not (isfinite(x) and isfinite(y)):
            raise ValueError(f"x={x} und y={y} muessen beide endlich sein.")
        #: die x-Koordinate des Punktes
        self.x: Final[int | float] = x
        #: die y-Koordinate des Punktes
        self.y: Final[int | float] = y

    def abstand(self, p: "Punkt") -> float:
        """
        Liefert den euklidischen Abstand zu einem anderen Punkt.

        :param p: der andere Punkt
        :return: der Abstand

        >>> Punkt(0, 0).abstand(Punkt(3, 4))
        5.0
        """
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)


    def __str__(self) -> str:
        """Knappe Darstellung fuer Endnutzer."""
        return f"({self.x}, {self.y})"


    def __repr__(self) -> str:
        """Darstellung fuer Programmierer."""
        return f"Punkt({self.x = }, {self.y = })"


    def __format__(self, format_spec: str) -> str:
        """Formatierte Darstellung."""
        return f"({self.x:{format_spec}}, {self.y:{format_spec}})"


    def __eq__(self, anderer) -> bool | NotImplementedType:
        """True, wenn anderer ebenfalls ein Punkt mit gleichen Koordinaten ist."""
        return (anderer.x == self.x) and (anderer.y == self.y) if isinstance(anderer, Punkt) else NotImplemented


    def __hash__(self) -> int:
        """Hashwert aus genau den Attributen, die auch __eq__ verwendet."""
        return hash((self.x, self.y))  # Tupel bilden, Tupel hashen