from math import isfinite, sqrt
from typing import Final

from mixins import JsonMixin


class Punkt(JsonMixin):
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
