from kreis import Kreis
from punkt import Punkt
from form import Form

kreis = Kreis(Punkt(2, 3), 5)
print(kreis.umfang())
print(kreis.flaeche())

print(isinstance(kreis, Kreis))
print(isinstance(kreis, Form))
print(isinstance(kreis, object))

print(issubclass(Kreis, Form))
print(issubclass(Form, Kreis))
print(issubclass(Form, object))