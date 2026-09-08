"""Die abstrakte Oberklasse Form."""

class Form():
    """Die gemeinsame Oberklasse aller geometrischen Formen."""

    # --------- was jede Unterklasse liefern muss ---------
    def flaeche(self) -> int | float:
        """Der Flaecheninhalt der Form."""
        raise NotImplementedError


    def umfang(self) -> int | float:
        """Der Umfang der Form."""
        raise NotImplementedError

