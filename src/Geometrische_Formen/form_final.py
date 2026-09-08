from abc import ABC, abstractmethod

from mixins import SortierMixin

class FormFinal(SortierMixin, ABC):
    """Die gemeinsame Oberklasse aller geometrischen Formen.

    `Form` erbt von zwei Seiten: von `SortierMixin` das Vergleichsverhalten und
    von `ABC` die Faehigkeit, abstrakt zu sein. Genau das ist Mehrfachvererbung –
    ein Verhaltensbaustein plus eine Basisklasse.

    Abstrakte Klassen lassen sich nicht instanziieren.
    """

    # ---------- was jede Unterklasse liefern muss ----------
    @abstractmethod
    def flaeche(self) -> float:
        """Der Flaecheninhalt der Form."""

    @abstractmethod
    def umfang(self) -> float:
        """Der Umfang der Form."""

    @abstractmethod
    def verschoben(self, dx: int | float, dy: int | float) -> "Form":
        """Aufgabe 6: eine NEUE, verschobene Form. Formen sind unveraenderlich."""

    # ---------- konkrete Methoden, die alle Formen erben ----------
    def beschreibung(self) -> str:
        """Flaeche und Umfang formatiert – geerbt von jeder Unterklasse."""
        return (f"{type(self).__name__}: Flaeche {self.flaeche():.3f}, "
                f"Umfang {self.umfang():.3f}")

    def kennwerte(self) -> dict:
        """Basis fuer TextMixin und JSONMixin – Unterklassen ergaenzen per super()."""
        return {"typ": type(self).__name__,
                "flaeche": round(self.flaeche(), 4),
                "umfang": round(self.umfang(), 4)}
