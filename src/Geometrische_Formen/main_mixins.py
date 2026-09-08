from punkt_mixin import Punkt
from kreis_mixin import Kreis

def main():
    print(Kreis(Punkt(0, 0), 1).to_json())

    print(Kreis(Punkt(0, 0), 1) < Kreis(Punkt(4, 4), 2))

    print([k.__name__ for k in Kreis.__mro__])

    print(Punkt(0, 0).to_json())

if __name__ == "__main__":
    main()