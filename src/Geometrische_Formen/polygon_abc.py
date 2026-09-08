"""Die zweite abstrakte Klasse – Polygon."""
from abc import ABC
from typing import Final, override

from form import Form
from punkt import Punkt


class Polygon(Form, ABC):
    """Alle Formen, die durch Eckpunkte beschrieben werden.

    Flaeche und Umfang berechnen sich fuer jedes Vieleck nach der gleichen Formel.

    Auch Polygon ist abstrakt.
    """

    def __init__(self, *ecken: Punkt) -> None:
        if len(ecken) < 3:
            raise ValueError("Ein Polygon braucht mindestens drei Ecken.")
        self.ecken: Final[tuple[Punkt, ...]] = tuple(ecken)

    def __repr__(self) -> str:
        return (f"{type(self).__name__}("+ ", ".join(repr(e) for e in self.ecken) + ")")

    @override
    def flaeche(self) -> float:
        """Gausssche Trapezformel (shoelace formula)."""
        summe: float = 0.0
        for i, ecke in enumerate(self.ecken):
            naechste: Punkt = self.ecken[(i + 1) % len(self.ecken)]
            summe += ecke.x * naechste.y - naechste.x * ecke.y
        return abs(summe) / 2

    @override
    def umfang(self) -> float:
        """Summe aller Kantenlaengen – die allgemeine Loesung."""
        return sum(ecke.abstand(self.ecken[(i + 1) % len(self.ecken)])
                   for i, ecke in enumerate(self.ecken))

    def kennwerte(self) -> dict:
        return super().kennwerte() | {"ecken": len(self.ecken)}
