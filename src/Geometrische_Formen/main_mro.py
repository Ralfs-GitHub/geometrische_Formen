from dreieck import Dreieck
from polygon import Polygon
from form_abc import Form

print([k.__name__ for k in Dreieck.__mro__])
print(Dreieck.mro())
help(Dreieck)

# Wo ist eine Methode tatsächlich implementiert?
print(Dreieck.umfang is Polygon.umfang)
print(Dreieck.flaeche is Polygon.flaeche)

# Alle direkten Basisklassen bzw. alle direkten Subklassen abfragen:
print(Dreieck.__bases__)
print(Form.__subclasses__())
