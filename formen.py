"""Geometrische Formen nach der vorgegebenen UML-Klassenhierarchie.

Die Implementierung verwendet ausschließlich Module aus der Python-Standardbibliothek.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from math import pi, sqrt
from typing import Iterable, Iterator


@dataclass(frozen=True)
class Punkt:
    """Unveränderlicher Punkt in der Ebene."""

    x: int | float
    y: int | float


class Form(ABC):
    """Abstrakte Oberklasse für geschlossene geometrische Formen."""

    @abstractmethod
    def flaeche(self) -> int | float:
        """Gibt die Fläche der Form zurück."""
        raise NotImplementedError

    @abstractmethod
    def umfang(self) -> int | float:
        """Gibt den Umfang der Form zurück."""
        raise NotImplementedError


class Kreis(Form):
    """Kreis mit einem Mittelpunkt und einem positiven Radius."""

    def __init__(self, center: Punkt, radius: int | float) -> None:
        """Erzeugt einen Kreis."""
        if not isinstance(center, Punkt):
            raise ValueError("center muss ein Punkt sein.")
        if not isinstance(radius, (int, float)) or isinstance(radius, bool):
            raise ValueError("radius muss eine Zahl sein.")
        if radius <= 0:
            raise ValueError("radius muss größer als 0 sein.")

        self.center = center
        self.radius = radius

    def flaeche(self) -> float:
        """Gibt die Kreisfläche zurück."""
        return pi * self.radius**2

    def umfang(self) -> float:
        """Gibt den Kreisumfang zurück."""
        return 2 * pi * self.radius


class Polygon(Form, ABC):
    """Abstrakte Oberklasse für Polygone."""

    @abstractmethod
    def punkte(self) -> Iterable[Punkt]:
        """Liefert die Eckpunkte des Polygons in ihrer Reihenfolge."""
        raise NotImplementedError

    def umfang(self) -> float:
        """Berechnet den Umfang aus den aufeinanderfolgenden Eckpunkten."""
        punkte = list(self.punkte())

        if len(punkte) < 3:
            raise ValueError("Ein Polygon benötigt mindestens drei Punkte.")

        umfang = 0.0
        for p1, p2 in zip(punkte, punkte[1:] + punkte[:1]):
            umfang += sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

        return umfang

    def print(self) -> None:
        """Gibt die wichtigsten Daten des Polygons aus."""
        print(f"Fläche: {self.flaeche()}")
        print(f"Umfang: {self.umfang()}")
        print(f"Punkte: {list(self.punkte())}")


class Rechteck(Polygon):
    """Rechteck, das durch zwei gegenüberliegende Ecken festgelegt wird."""

    def __init__(self, p1: Punkt, p2: Punkt) -> None:
        """Erzeugt ein achsenparalleles Rechteck aus zwei gegenüberliegenden Ecken."""
        if not isinstance(p1, Punkt) or not isinstance(p2, Punkt):
            raise ValueError("p1 und p2 müssen Punkte sein.")
        if p1.x == p2.x or p1.y == p2.y:
            raise ValueError("p1 und p2 müssen unterschiedliche x- und y-Koordinaten haben.")

        self.p1 = p1
        self.p2 = p2

    def flaeche(self) -> float:
        """Gibt die Rechteckfläche zurück."""
        breite = abs(self.p2.x - self.p1.x)
        hoehe = abs(self.p2.y - self.p1.y)
        return breite * hoehe

    def umfang(self) -> float:
        """Gibt den Rechteckumfang zurück."""
        breite = abs(self.p2.x - self.p1.x)
        hoehe = abs(self.p2.y - self.p1.y)
        return 2 * (breite + hoehe)

    def punkte(self) -> Iterator[Punkt]:
        """Liefert die vier Eckpunkte des achsenparallelen Rechtecks."""
        x_min = min(self.p1.x, self.p2.x)
        x_max = max(self.p1.x, self.p2.x)
        y_min = min(self.p1.y, self.p2.y)
        y_max = max(self.p1.y, self.p2.y)

        yield Punkt(x_min, y_min)
        yield Punkt(x_max, y_min)
        yield Punkt(x_max, y_max)
        yield Punkt(x_min, y_max)


class Dreieck(Polygon):
    """Dreieck, das durch drei Eckpunkte festgelegt wird."""

    def __init__(self, p1: Punkt, p2: Punkt, p3: Punkt) -> None:
        """Erzeugt ein Dreieck aus drei nicht kollinearen Punkten."""
        if not all(isinstance(p, Punkt) for p in (p1, p2, p3)):
            raise ValueError("p1, p2 und p3 müssen Punkte sein.")

        doppelte_punkte = len({p1, p2, p3}) != 3
        if doppelte_punkte:
            raise ValueError("Ein Dreieck benötigt drei verschiedene Punkte.")

        doppelter_flaecheninhalt = (
            (p2.x - p1.x) * (p3.y - p1.y)
            - (p2.y - p1.y) * (p3.x - p1.x)
        )
        if doppelter_flaecheninhalt == 0:
            raise ValueError("Die drei Punkte dürfen nicht auf einer Geraden liegen.")

        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def flaeche(self) -> float:
        """Gibt die Dreiecksfläche zurück."""
        return abs(
            (self.p1.x * (self.p2.y - self.p3.y)
             + self.p2.x * (self.p3.y - self.p1.y)
             + self.p3.x * (self.p1.y - self.p2.y))
            / 2
        )

    def punkte(self) -> tuple[Punkt, Punkt, Punkt]:
        """Liefert die drei Eckpunkte des Dreiecks."""
        return self.p1, self.p2, self.p3


class Quadrat(Rechteck):
    """Rechteck mit vier gleich langen Seiten.

    Das Quadrat überschreibt keine der drei Operationen flaeche(), umfang()
    und punkte(), sondern verwendet die Implementierungen von Rechteck bzw.
    Polygon.
    """

    def __init__(self, p1: Punkt, seite: int | float) -> None:
        """Erzeugt ein achsenparalleles Quadrat aus einer Ecke und der Seitenlänge."""
        if not isinstance(p1, Punkt):
            raise ValueError("p1 muss ein Punkt sein.")
        if not isinstance(seite, (int, float)) or isinstance(seite, bool):
            raise ValueError("seite muss eine Zahl sein.")
        if seite <= 0:
            raise ValueError("seite muss größer als 0 sein.")

        self.seite = seite

        # Das zweite Rechteckattribut wird aus Ecke und Seitenlänge abgeleitet.
        p2 = Punkt(p1.x + seite, p1.y + seite)
        super().__init__(p1, p2)


if __name__ == "__main__":
    quadrat = Quadrat(Punkt(0, 0), 4)
    print(f"Quadratfläche: {quadrat.flaeche()}")
    print(f"Quadratumfang: {quadrat.umfang()}")
