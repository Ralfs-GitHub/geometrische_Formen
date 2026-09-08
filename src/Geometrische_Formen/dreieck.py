"""Das Dreieck – nutzt umfang() unveraendert aus Polygon."""
from punkt import Punkt
from polygon import Polygon
from typing import Final, override

class Dreieck(Polygon):
    """Ein Dreieck, festgelegt durch drei Eckpunkte.
    """

    def __init__(self, p1: Punkt, p2: Punkt, p3: Punkt) -> None:
        if (p1.abstand(p2) <= 0) or (p2.abstand(p3) <= 0) or (p3.abstand(p1) <= 0):      # Seite der Laenge 0?
            raise ValueError("entartetes Dreieck")
        self.p1: Final[Punkt] = p1
        self.p2: Final[Punkt] = p2
        self.p3: Final[Punkt] = p3


    @override
    def punkte(self) -> tuple[Punkt, Punkt, Punkt]:
        return self.p1, self.p2, self.p3


    @override
    def flaeche(self) -> int | float:
        # Formel aus der Schulmathematik
        return 0.5 * abs(self.p1.x * (self.p2.y - self.p3.y)
                         + self.p2.x * (self.p3.y - self.p1.y)
                         + self.p3.x * (self.p1.y - self.p2.y))
