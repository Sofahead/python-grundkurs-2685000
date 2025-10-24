"""
Taschenrechner-Modul mit grundlegenden mathematischen Operationen.

Dieses Modul demonstriert Best Practices wie:
- Aussagekräftige Funktionsnamen
- Type Hints für bessere Lesbarkeit
- Docstrings für Dokumentation
- Fehlerbehandlung für robusteren Code
"""

from typing import Union


def addiere(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Addiert zwei Zahlen.
    
    Args:
        a: Die erste Zahl
        b: Die zweite Zahl
    
    Returns:
        Die Summe von a und b
    
    Beispiel:
        >>> addiere(5, 3)
        8
    """
    return a + b


def subtrahiere(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Subtrahiert die zweite Zahl von der ersten.
    
    Args:
        a: Die Zahl, von der subtrahiert wird
        b: Die Zahl, die subtrahiert wird
    
    Returns:
        Die Differenz von a und b
    
    Beispiel:
        >>> subtrahiere(10, 4)
        6
    """
    return a - b


def multipliziere(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Multipliziert zwei Zahlen.
    
    Args:
        a: Die erste Zahl
        b: Die zweite Zahl
    
    Returns:
        Das Produkt von a und b
    
    Beispiel:
        >>> multipliziere(4, 5)
        20
    """
    return a * b


def dividiere(a: Union[int, float], b: Union[int, float]) -> float:
    """
    Dividiert die erste Zahl durch die zweite.
    
    Args:
        a: Der Dividend
        b: Der Divisor
    
    Returns:
        Der Quotient von a und b
    
    Raises:
        ValueError: Wenn b gleich 0 ist
    
    Beispiel:
        >>> dividiere(10, 2)
        5.0
    """
    if b == 0:
        raise ValueError("Division durch Null ist nicht erlaubt")
    return a / b


def potenz(basis: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """
    Berechnet die Potenz einer Zahl.
    
    Args:
        basis: Die Basis
        exponent: Der Exponent
    
    Returns:
        Das Ergebnis von basis^exponent
    
    Beispiel:
        >>> potenz(2, 3)
        8
    """
    return basis ** exponent


def main():
    """Demonstriert die Verwendung der Taschenrechner-Funktionen."""
    print("=== Taschenrechner Beispiele ===\n")
    
    # Addition
    ergebnis = addiere(15, 7)
    print(f"15 + 7 = {ergebnis}")
    
    # Subtraktion
    ergebnis = subtrahiere(20, 8)
    print(f"20 - 8 = {ergebnis}")
    
    # Multiplikation
    ergebnis = multipliziere(6, 7)
    print(f"6 × 7 = {ergebnis}")
    
    # Division
    ergebnis = dividiere(100, 4)
    print(f"100 ÷ 4 = {ergebnis}")
    
    # Potenz
    ergebnis = potenz(2, 10)
    print(f"2^10 = {ergebnis}")
    
    # Fehlerbehandlung demonstrieren
    print("\n=== Fehlerbehandlung ===")
    try:
        ergebnis = dividiere(10, 0)
    except ValueError as e:
        print(f"Fehler: {e}")


if __name__ == "__main__":
    main()
