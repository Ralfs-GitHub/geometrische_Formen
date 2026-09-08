"""Die abstrakte Oberklasse Form."""
from abc import ABC, abstractmethod

class Form(ABC):
    """Die gemeinsame Oberklasse aller geometrischen Formen.

    `Form` erbt von `ABC` die Faehigkeit, abstrakt zu sein.
    Abstrakte Klassen lassen sich nicht instanziieren.
    """
    @abstractmethod
    def flaeche(self) -> float:
        """Der Flaecheninhalt der Form."""

    @abstractmethod
    def umfang(self) -> float:
        """Der Umfang der Form."""