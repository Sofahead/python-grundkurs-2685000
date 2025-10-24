"""
Hauptprogramm - Demonstration aller Module zusammen.

Dieses Programm zeigt:
- Import und Verwendung mehrerer Module
- Strukturierte Programmorganisation
- Benutzerinteraktion (optional)
- Best Practices für Hauptprogramme
"""

import sys
from datetime import datetime

# Lokale Module importieren
import calculator
import daten_verarbeitung
import datei_operationen
import klassen_beispiel
import utilities


def zeige_menu() -> None:
    """Zeigt das Hauptmenü an."""
    print("\n" + "=" * 60)
    print("  PYTHON GRUNDKURS - BEST PRACTICES DEMONSTRATION")
    print("=" * 60)
    print("\nVerfügbare Demos:")
    print("  1. Taschenrechner (calculator.py)")
    print("  2. Datenverarbeitung (daten_verarbeitung.py)")
    print("  3. Dateioperationen (datei_operationen.py)")
    print("  4. Klassen und Objekte (klassen_beispiel.py)")
    print("  5. Utility-Funktionen (utilities.py)")
    print("  6. Alle Demos nacheinander")
    print("  0. Beenden")
    print("-" * 60)


def fuehre_calculator_demo() -> None:
    """Führt die Taschenrechner-Demo aus."""
    print("\n" + "=" * 60)
    print("DEMO: TASCHENRECHNER")
    print("=" * 60)
    calculator.main()


def fuehre_daten_demo() -> None:
    """Führt die Datenverarbeitungs-Demo aus."""
    print("\n" + "=" * 60)
    print("DEMO: DATENVERARBEITUNG")
    print("=" * 60)
    daten_verarbeitung.main()


def fuehre_datei_demo() -> None:
    """Führt die Dateioperations-Demo aus."""
    print("\n" + "=" * 60)
    print("DEMO: DATEIOPERATIONEN")
    print("=" * 60)
    datei_operationen.main()


def fuehre_klassen_demo() -> None:
    """Führt die Klassen-Demo aus."""
    print("\n" + "=" * 60)
    print("DEMO: KLASSEN UND OBJEKTE")
    print("=" * 60)
    klassen_beispiel.main()


def fuehre_utilities_demo() -> None:
    """Führt die Utilities-Demo aus."""
    print("\n" + "=" * 60)
    print("DEMO: UTILITY-FUNKTIONEN")
    print("=" * 60)
    utilities.main()


def fuehre_alle_demos(interaktiv: bool = True) -> None:
    """
    Führt alle Demos nacheinander aus.
    
    Args:
        interaktiv: Wenn True, wartet auf Benutzereingabe zwischen Demos
    """
    demos = [
        fuehre_calculator_demo,
        fuehre_daten_demo,
        fuehre_datei_demo,
        fuehre_klassen_demo,
        fuehre_utilities_demo
    ]
    
    for i, demo in enumerate(demos):
        demo()
        if i < len(demos) - 1:  # Nicht nach der letzten Demo
            print("\n" + "-" * 60)
            if interaktiv:
                input("Drücken Sie Enter für die nächste Demo...")
            else:
                print("Nächste Demo wird gestartet...\n")


def zeige_zusammenfassung() -> None:
    """Zeigt eine Zusammenfassung der Best Practices."""
    print("\n" + "=" * 60)
    print("PYTHON BEST PRACTICES - ZUSAMMENFASSUNG")
    print("=" * 60)
    print("""
1. CODE-STRUKTUR:
   ✓ Aussagekräftige Funktions- und Variablennamen
   ✓ Modulare Organisation in separate Dateien
   ✓ Ein Modul pro Verantwortungsbereich
   
2. DOKUMENTATION:
   ✓ Docstrings für Module, Klassen und Funktionen
   ✓ Type Hints für bessere Lesbarkeit
   ✓ Kommentare wo nötig, aber Code sollte selbsterklärend sein
   
3. FEHLERBEHANDLUNG:
   ✓ Try-Except-Blöcke für I/O-Operationen
   ✓ Validierung von Eingabedaten
   ✓ Aussagekräftige Fehlermeldungen
   
4. OBJEKTORIENTIERUNG:
   ✓ Klassen für zusammengehörige Daten und Methoden
   ✓ Datenkapselung mit privaten Attributen (_attribut)
   ✓ Properties für kontrollierten Zugriff
   
5. FUNKTIONALE PROGRAMMIERUNG:
   ✓ List Comprehensions für prägnanten Code
   ✓ Lambda-Funktionen für einfache Operationen
   ✓ Reine Funktionen ohne Seiteneffekte
   
6. DATEIEN UND I/O:
   ✓ Context Manager (with) für sichere Dateioperationen
   ✓ UTF-8 Encoding explizit angeben
   ✓ Pfad-Handling mit pathlib
   
7. PEP 8 STIL:
   ✓ 4 Leerzeichen für Einrückung
   ✓ Maximale Zeilenlänge von 79-100 Zeichen
   ✓ Leerzeilen zur Strukturierung
   ✓ Konsistente Namenskonventionen

8. TESTING UND QUALITÄT:
   ✓ Doctest-Beispiele in Docstrings
   ✓ Eingabevalidierung
   ✓ Defensive Programmierung
    """)
    print("=" * 60)


def interaktiver_modus() -> None:
    """Führt das Programm im interaktiven Modus aus."""
    while True:
        zeige_menu()
        
        try:
            auswahl = input("\nBitte wählen Sie eine Option (0-6): ").strip()
            
            if auswahl == '0':
                print("\nAuf Wiedersehen! 👋")
                break
            elif auswahl == '1':
                fuehre_calculator_demo()
            elif auswahl == '2':
                fuehre_daten_demo()
            elif auswahl == '3':
                fuehre_datei_demo()
            elif auswahl == '4':
                fuehre_klassen_demo()
            elif auswahl == '5':
                fuehre_utilities_demo()
            elif auswahl == '6':
                fuehre_alle_demos(interaktiv=True)
            else:
                print("\n⚠ Ungültige Auswahl. Bitte wählen Sie 0-6.")
            
            if auswahl in ['1', '2', '3', '4', '5']:
                input("\nDrücken Sie Enter, um zum Menü zurückzukehren...")
                
        except KeyboardInterrupt:
            print("\n\nProgramm durch Benutzer abgebrochen.")
            break
        except Exception as e:
            print(f"\n⚠ Ein Fehler ist aufgetreten: {e}")


def automatischer_modus() -> None:
    """Führt alle Demos automatisch aus (für nicht-interaktive Umgebungen)."""
    print("\n🤖 Automatischer Modus - Alle Demos werden ausgeführt\n")
    fuehre_alle_demos(interaktiv=False)
    zeige_zusammenfassung()


def main() -> None:
    """
    Haupteinstiegspunkt des Programms.
    
    Erkennt, ob das Programm interaktiv ausgeführt wird
    und wählt entsprechend den passenden Modus.
    """
    print("\n" + "=" * 60)
    print("  WILLKOMMEN ZUM PYTHON GRUNDKURS")
    print("  Best Practices und Code-Qualität")
    print("=" * 60)
    print(f"\nStartzeit: {utilities.formatiere_datum(datetime.now(), 'mittel')}")
    
    # Prüfen ob stdin interaktiv ist
    if sys.stdin.isatty():
        # Interaktiver Modus (Terminal)
        try:
            interaktiver_modus()
        except Exception as e:
            print(f"\nFehler im interaktiven Modus: {e}")
            print("Wechsle zum automatischen Modus...\n")
            automatischer_modus()
    else:
        # Automatischer Modus (z.B. in CI/CD oder Skript)
        automatischer_modus()
    
    print("\n" + "=" * 60)
    print("  Programm beendet")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
