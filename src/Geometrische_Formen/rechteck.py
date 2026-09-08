from typing import Final

from punkt import Punkt
from polygon import Polygon


class Rechteck(Polygon):
    """Ein Rechteck definiert durch seine unteren linken und oberen rechten Eckpunkte."""

    def __init__(self, p1: Punkt, p2: Punkt) -> None:
        """
        Erstelle ein Rechteck.

        :param p1: der erste Punkt, der das Rechteck aufspannt
        :param p2: der zweite Punkt, der das Rechteck aufspannt
        """
        if (p1.x == p2.x) or (p1.y == p2.y):
            raise ValueError(f"{p1.x},{p1.y},{p2.x},{p2.y} ist leer.")

        #: der untere linke Punkt, der das Rechteck aufspannt
        self.p1: Final[Punkt] = Punkt(min(p1.x, p2.x), min(p1.y, p2.y))

        #: der obere rechte Punkt, der das Rechteck aufspannt
        self.p2: Final[Punkt] = Punkt(max(p1.x, p2.x), max(p1.y, p2.y))


    def flaeche(self) -> int | float:
        """
        Gib die Fläche dieses Rechtecks zurück.

        :return: die Fläche dieses Rechtecks

        >>> Rechteck(Punkt(7, 3), Punkt(12, 6)).flaeche()
        15
        """
        return (self.p2.x - self.p1.x) * (self.p2.y - self.p1.y)


    def umfang(self) -> int | float:
        """
        Gib den Umfang dieses Rechtecks zurück.

        :return: den Umfang dieses Rechtecks

        >>> Rechteck(Punkt(10, 5), Punkt(4, 9)).umfang()
        20
        """
        return 2 * ((self.p2.x - self.p1.x) + (self.p2.y - self.p1.y))


    def punkte(self) -> tuple[Punkt, Punkt, Punkt, Punkt]:
        """
        Gib die vier Eckpunkte dieses Rechtecks zurück.

        :return: ein Tupel mit den vier Eckpunkten dieses Rechtecks
        """
        return (self.p1, Punkt(self.p1.x, self.p2.y), self.p2, Punkt(self.p2.x, self.p1.y))
