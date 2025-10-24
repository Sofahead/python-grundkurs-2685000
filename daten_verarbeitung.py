"""
Modul für Datenverarbeitung mit Best Practices.

Dieses Modul zeigt:
- Verwendung von Listen und Dictionaries
- List Comprehensions für prägnanten Code
- Type Hints für komplexe Datentypen
- Defensive Programmierung
"""

from typing import List, Dict, Optional, Any, Union


def filtere_gerade_zahlen(zahlen: List[int]) -> List[int]:
    """
    Filtert gerade Zahlen aus einer Liste.
    
    Args:
        zahlen: Eine Liste von Ganzzahlen
    
    Returns:
        Eine neue Liste mit nur geraden Zahlen
    
    Beispiel:
        >>> filtere_gerade_zahlen([1, 2, 3, 4, 5, 6])
        [2, 4, 6]
    """
    return [zahl for zahl in zahlen if zahl % 2 == 0]


def berechne_durchschnitt(zahlen: List[Union[int, float]]) -> Optional[float]:
    """
    Berechnet den Durchschnitt einer Zahlenliste.
    
    Args:
        zahlen: Eine Liste von Zahlen
    
    Returns:
        Der Durchschnitt oder None bei leerer Liste
    
    Beispiel:
        >>> berechne_durchschnitt([10, 20, 30])
        20.0
    """
    if not zahlen:
        return None
    return sum(zahlen) / len(zahlen)


def gruppiere_nach_laenge(woerter: List[str]) -> Dict[int, List[str]]:
    """
    Gruppiert Wörter nach ihrer Länge.
    
    Args:
        woerter: Eine Liste von Wörtern
    
    Returns:
        Ein Dictionary mit Länge als Schlüssel und Wortlisten als Werte
    
    Beispiel:
        >>> gruppiere_nach_laenge(['Hallo', 'Welt', 'Python'])
        {5: ['Hallo'], 4: ['Welt'], 6: ['Python']}
    """
    gruppen: Dict[int, List[str]] = {}
    
    for wort in woerter:
        laenge = len(wort)
        if laenge not in gruppen:
            gruppen[laenge] = []
        gruppen[laenge].append(wort)
    
    return gruppen


def erstelle_statistik(daten: List[Union[int, float]]) -> Dict[str, Any]:
    """
    Erstellt eine Statistik-Übersicht für eine Datenliste.
    
    Args:
        daten: Eine Liste von Zahlen
    
    Returns:
        Ein Dictionary mit statistischen Kennzahlen
    
    Beispiel:
        >>> statistik = erstelle_statistik([1, 2, 3, 4, 5])
        >>> statistik['minimum']
        1
    """
    if not daten:
        return {
            'anzahl': 0,
            'summe': 0,
            'durchschnitt': None,
            'minimum': None,
            'maximum': None
        }
    
    return {
        'anzahl': len(daten),
        'summe': sum(daten),
        'durchschnitt': sum(daten) / len(daten),
        'minimum': min(daten),
        'maximum': max(daten)
    }


def bereinige_text(text: str) -> str:
    """
    Bereinigt einen Text durch Entfernen von führenden/nachfolgenden Leerzeichen
    und Konvertierung zu Kleinbuchstaben.
    
    Args:
        text: Der zu bereinigende Text
    
    Returns:
        Der bereinigte Text
    
    Beispiel:
        >>> bereinige_text("  HELLO World  ")
        'hello world'
    """
    return text.strip().lower()


def main():
    """Demonstriert die Datenverarbeitungsfunktionen."""
    print("=== Datenverarbeitung Beispiele ===\n")
    
    # Zahlen filtern
    zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    gerade = filtere_gerade_zahlen(zahlen)
    print(f"Gerade Zahlen aus {zahlen}:")
    print(f"  {gerade}\n")
    
    # Durchschnitt berechnen
    noten = [1.0, 2.3, 1.7, 2.0, 1.3]
    durchschnitt = berechne_durchschnitt(noten)
    print(f"Durchschnittsnote: {durchschnitt:.2f}\n")
    
    # Wörter gruppieren
    woerter = ['Python', 'Java', 'C', 'JavaScript', 'Go', 'Ruby', 'Rust']
    gruppiert = gruppiere_nach_laenge(woerter)
    print("Programmiersprachen nach Namenslänge:")
    for laenge, sprachen in sorted(gruppiert.items()):
        print(f"  {laenge} Zeichen: {', '.join(sprachen)}")
    print()
    
    # Statistik erstellen
    messwerte = [23.5, 24.1, 23.8, 24.5, 23.2, 24.0, 23.7]
    statistik = erstelle_statistik(messwerte)
    print("Temperatur-Statistik:")
    print(f"  Anzahl Messungen: {statistik['anzahl']}")
    print(f"  Durchschnitt: {statistik['durchschnitt']:.2f}°C")
    print(f"  Minimum: {statistik['minimum']:.2f}°C")
    print(f"  Maximum: {statistik['maximum']:.2f}°C")


if __name__ == "__main__":
    from typing import Union
    main()
