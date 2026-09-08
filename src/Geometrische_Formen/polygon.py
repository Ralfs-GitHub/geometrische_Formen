"""A polygon is a figure described by its corner points."""
from typing import Iterable, Final, override

from punkt import Punkt
from form import Form


class Polygon(Form):
    """Vielecke sind Formen, die von geraden Strecken begrenzt werden."""
    def __init__(self, *ecken: Punkt) -> None:
        if len(ecken) < 3:
            raise ValueError("Ein Vieleck braucht mindestens drei Ecken.")
        self.ecken: Final[tuple[Punkt, ...]] = tuple(ecken)


    def punkte(self) -> Iterable[Punkt]:
        """Liefert die Eckpunkte dieses Polygons."""
        raise NotImplementedError   # muss die Subklasse implementieren


    @override
    def umfang(self) -> int | float:
        vorheriger: Punkt | None = None
        erster: Punkt | None = None
        summe: float = 0.0                  # gewoehnliche Summation
        for aktueller in self.punkte():     # ruft die SUBKLASSE auf
            if vorheriger is None:
                vorheriger = erster = aktueller   # ersten Punkt merken
            else:
                summe += vorheriger.abstand(aktueller)
                vorheriger = aktueller
        summe += vorheriger.abstand(erster)   # Kante zurueck zum Start
        return summe


    @override
    def flaeche(self) -> float:
        """Gausssche Trapezformel (shoelace formula)."""
        summe: float = 0.0
        for i, ecke in enumerate(self.ecken):
            naechste: Punkt = self.ecken[(i + 1) % len(self.ecken)]
            summe += ecke.x * naechste.y - naechste.x * ecke.y
        return abs(summe) / 2


    def print(self) -> None:
        """Ausgabe der Punkte des Polygons."""
        print(", ".join(f"({p.x}, {p.y})" for p in self.punkte()))
