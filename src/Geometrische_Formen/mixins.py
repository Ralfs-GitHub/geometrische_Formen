import json
from types import NotImplementedType


class SortierMixin:
    """Ordnung und Gleichheit auf Basis der Flaeche.

    Setzt voraus, dass die Klasse eine Methode `flaeche()` besitzt.

    Wer `__eq__` definiert, bekommt von Python automatisch
    `__hash__ = None` gesetzt. Die Klasse waere dann nicht
    mehr hashbar. Deshalb wird `__hash__` hier wieder gesetzt.
    """

    def __eq__(self, andere) -> bool | NotImplementedType:
        return self.flaeche() == andere.flaeche() \
            if hasattr(andere, "flaeche") else NotImplemented

    def __lt__(self, andere) -> bool | NotImplementedType:
        return self.flaeche() < andere.flaeche() \
            if hasattr(andere, "flaeche") else NotImplemented

    def __hash__(self) -> int:
        """Gleiche Flaeche muss den gleichen Hashwert liefern -> Vertrag mit __eq__."""
        return hash(round(self.flaeche(), 9))


class VergleichMixin:
    def __lt__(self, andere) -> bool | NotImplementedType:
        return self.flaeche() < andere.flaeche() \
            if hasattr(andere, "flaeche") else NotImplemented


class TextMixin:
    """Eine lesbare Textdarstellung aus den Kennwerten der Klasse.

    Setzt voraus, dass die Klasse eine Methode `kennwerte()` besitzt.
    """

    def __str__(self) -> str:
        werte = self.kennwerte()
        typ = werte.pop("typ")
        rest = ", ".join(f"{name}={wert}" for name, wert in werte.items())
        return f"{typ}({rest})"


class JsonMixin:
    def to_dict(self) -> dict:
        return self.__dict__

    """Serialisierung nach JSON."""
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)
