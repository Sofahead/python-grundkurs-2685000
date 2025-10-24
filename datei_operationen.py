"""
Modul für Dateioperationen mit Best Practices.

Dieses Modul demonstriert:
- Sichere Dateioperationen mit Context Managern
- Fehlerbehandlung für I/O-Operationen
- Arbeiten mit verschiedenen Dateiformaten
- Pfad-Handling mit pathlib
"""

import json
from pathlib import Path
from typing import List, Dict, Optional, Any


def lies_textdatei(dateipfad: str) -> Optional[str]:
    """
    Liest den Inhalt einer Textdatei sicher ein.
    
    Args:
        dateipfad: Pfad zur Textdatei
    
    Returns:
        Der Inhalt der Datei oder None bei Fehler
    
    Beispiel:
        >>> inhalt = lies_textdatei('beispiel.txt')
    """
    try:
        with open(dateipfad, 'r', encoding='utf-8') as datei:
            return datei.read()
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateipfad}' nicht gefunden")
        return None
    except PermissionError:
        print(f"Fehler: Keine Berechtigung für '{dateipfad}'")
        return None
    except Exception as e:
        print(f"Unerwarteter Fehler beim Lesen: {e}")
        return None


def schreibe_textdatei(dateipfad: str, inhalt: str) -> bool:
    """
    Schreibt Text in eine Datei.
    
    Args:
        dateipfad: Pfad zur Zieldatei
        inhalt: Der zu schreibende Text
    
    Returns:
        True bei Erfolg, False bei Fehler
    
    Beispiel:
        >>> erfolg = schreibe_textdatei('ausgabe.txt', 'Hallo Welt')
    """
    try:
        with open(dateipfad, 'w', encoding='utf-8') as datei:
            datei.write(inhalt)
        return True
    except PermissionError:
        print(f"Fehler: Keine Schreibberechtigung für '{dateipfad}'")
        return False
    except Exception as e:
        print(f"Unerwarteter Fehler beim Schreiben: {e}")
        return False


def lies_zeilen(dateipfad: str) -> List[str]:
    """
    Liest alle Zeilen einer Datei in eine Liste.
    
    Args:
        dateipfad: Pfad zur Textdatei
    
    Returns:
        Liste mit allen Zeilen (ohne Zeilenumbrüche)
    
    Beispiel:
        >>> zeilen = lies_zeilen('daten.txt')
    """
    try:
        with open(dateipfad, 'r', encoding='utf-8') as datei:
            return [zeile.strip() for zeile in datei.readlines()]
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateipfad}' nicht gefunden")
        return []
    except Exception as e:
        print(f"Fehler beim Lesen: {e}")
        return []


def speichere_json(dateipfad: str, daten: Any) -> bool:
    """
    Speichert Daten im JSON-Format.
    
    Args:
        dateipfad: Pfad zur JSON-Datei
        daten: Die zu speichernden Daten (muss JSON-serialisierbar sein)
    
    Returns:
        True bei Erfolg, False bei Fehler
    
    Beispiel:
        >>> erfolg = speichere_json('daten.json', {'name': 'Max', 'alter': 25})
    """
    try:
        with open(dateipfad, 'w', encoding='utf-8') as datei:
            json.dump(daten, datei, ensure_ascii=False, indent=2)
        return True
    except TypeError as e:
        print(f"Fehler: Daten nicht JSON-serialisierbar: {e}")
        return False
    except Exception as e:
        print(f"Fehler beim Speichern: {e}")
        return False


def lade_json(dateipfad: str) -> Optional[Any]:
    """
    Lädt Daten aus einer JSON-Datei.
    
    Args:
        dateipfad: Pfad zur JSON-Datei
    
    Returns:
        Die geladenen Daten oder None bei Fehler
    
    Beispiel:
        >>> daten = lade_json('daten.json')
    """
    try:
        with open(dateipfad, 'r', encoding='utf-8') as datei:
            return json.load(datei)
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateipfad}' nicht gefunden")
        return None
    except json.JSONDecodeError as e:
        print(f"Fehler: Ungültiges JSON-Format: {e}")
        return None
    except Exception as e:
        print(f"Fehler beim Laden: {e}")
        return None


def erstelle_verzeichnis(verzeichnis: str) -> bool:
    """
    Erstellt ein Verzeichnis, falls es noch nicht existiert.
    
    Args:
        verzeichnis: Pfad zum zu erstellenden Verzeichnis
    
    Returns:
        True bei Erfolg oder wenn Verzeichnis bereits existiert
    
    Beispiel:
        >>> erstelle_verzeichnis('ausgabe/berichte')
    """
    try:
        pfad = Path(verzeichnis)
        pfad.mkdir(parents=True, exist_ok=True)
        return True
    except PermissionError:
        print(f"Fehler: Keine Berechtigung zum Erstellen von '{verzeichnis}'")
        return False
    except Exception as e:
        print(f"Fehler beim Erstellen des Verzeichnisses: {e}")
        return False


def main():
    """Demonstriert die Dateioperationen."""
    print("=== Dateioperationen Beispiele ===\n")
    
    # Temporäres Verzeichnis erstellen
    temp_ordner = '/tmp/python_beispiele'
    if erstelle_verzeichnis(temp_ordner):
        print(f"✓ Verzeichnis erstellt: {temp_ordner}\n")
    
    # Text in Datei schreiben
    text_datei = f'{temp_ordner}/beispiel.txt'
    beispieltext = """Dies ist eine Beispieldatei.
Sie zeigt, wie man Text sicher in Dateien schreibt.
Mit mehreren Zeilen."""
    
    if schreibe_textdatei(text_datei, beispieltext):
        print(f"✓ Text gespeichert in: {text_datei}")
    
    # Text aus Datei lesen
    gelesener_text = lies_textdatei(text_datei)
    if gelesener_text:
        print(f"✓ Text gelesen ({len(gelesener_text)} Zeichen)\n")
    
    # JSON-Daten speichern
    json_datei = f'{temp_ordner}/daten.json'
    beispiel_daten = {
        'kurs': 'Python Grundkurs',
        'teilnehmer': 25,
        'themen': ['Variablen', 'Funktionen', 'Klassen', 'Module'],
        'aktiv': True
    }
    
    if speichere_json(json_datei, beispiel_daten):
        print(f"✓ JSON gespeichert in: {json_datei}")
    
    # JSON-Daten laden
    geladene_daten = lade_json(json_datei)
    if geladene_daten:
        print(f"✓ JSON geladen: {geladene_daten['kurs']}")
        print(f"  Themen: {', '.join(geladene_daten['themen'])}\n")
    
    # Zeilen lesen
    zeilen = lies_zeilen(text_datei)
    print(f"Datei hat {len(zeilen)} Zeilen")
    
    print(f"\n✓ Alle Beispieldateien wurden in '{temp_ordner}' erstellt")


if __name__ == "__main__":
    main()
