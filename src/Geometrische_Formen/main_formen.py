from kreis import Kreis
from punkt import Punkt
from rechteck import Rechteck
from dreieck import Dreieck
from form import Form

def main():
    formen: list[Form] = [
        Kreis(Punkt(2, 3), 5),
        Rechteck(Punkt(2, 3), Punkt(3, 5)),
        Dreieck(Punkt(2, 3), Punkt(3, 5), Punkt(7, 4)),
    ]

    for f in formen:
        print(f"{type(f).__name__:<10}: "
              f" A={f.flaeche():<5.2f} and U={f.umfang():.2f}")


if __name__ == "__main__":
    main()
