"""
Utility-Modul mit nützlichen Hilfsfunktionen.

Dieses Modul zeigt:
- Wiederverwendbare Funktionen
- Eingabevalidierung
- String-Manipulation
- Datum/Zeit-Funktionen
"""

import re
from datetime import datetime, timedelta
from typing import Optional, List


def ist_gueltige_email(email: str) -> bool:
    """
    Prüft, ob eine E-Mail-Adresse gültig ist.
    
    Args:
        email: Die zu prüfende E-Mail-Adresse
    
    Returns:
        True wenn gültig, sonst False
    
    Beispiel:
        >>> ist_gueltige_email('max@beispiel.de')
        True
        >>> ist_gueltige_email('ungueltig')
        False
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def formatiere_telefonnummer(nummer: str) -> Optional[str]:
    """
    Formatiert eine Telefonnummer in ein einheitliches Format.
    
    Args:
        nummer: Die unformatierte Telefonnummer
    
    Returns:
        Die formatierte Nummer oder None bei ungültiger Eingabe
    
    Beispiel:
        >>> formatiere_telefonnummer('01701234567')
        '+49 170 1234567'
    """
    # Entferne alle nicht-numerischen Zeichen
    nur_zahlen = re.sub(r'\D', '', nummer)
    
    # Deutsche Mobilnummer (0170... -> +49 170...)
    if nur_zahlen.startswith('0') and len(nur_zahlen) == 11:
        return f'+49 {nur_zahlen[1:4]} {nur_zahlen[4:]}'
    
    return None


def verkuerze_text(text: str, max_laenge: int = 50, suffix: str = '...') -> str:
    """
    Verkürzt einen Text auf eine maximale Länge.
    
    Args:
        text: Der zu verkürzende Text
        max_laenge: Maximale Länge (Standard: 50)
        suffix: Suffix für verkürzte Texte (Standard: '...')
    
    Returns:
        Der (möglicherweise verkürzte) Text
    
    Beispiel:
        >>> verkuerze_text('Ein sehr langer Text der verkürzt werden soll', 20)
        'Ein sehr langer T...'
    """
    if len(text) <= max_laenge:
        return text
    
    return text[:max_laenge - len(suffix)] + suffix


def kapitalisiere_woerter(text: str) -> str:
    """
    Kapitalisiert den ersten Buchstaben jedes Wortes.
    
    Args:
        text: Der zu kapitalisierende Text
    
    Returns:
        Der Text mit kapitalisierten Wörtern
    
    Beispiel:
        >>> kapitalisiere_woerter('python ist toll')
        'Python Ist Toll'
    """
    return ' '.join(wort.capitalize() for wort in text.split())


def formatiere_datum(datum: datetime, format_typ: str = 'kurz') -> str:
    """
    Formatiert ein Datum in verschiedenen Formaten.
    
    Args:
        datum: Das zu formatierende Datum
        format_typ: 'kurz', 'mittel' oder 'lang' (Standard: 'kurz')
    
    Returns:
        Das formatierte Datum als String
    
    Beispiel:
        >>> jetzt = datetime.now()
        >>> formatiere_datum(jetzt, 'lang')
        '24. Oktober 2025'
    """
    formate = {
        'kurz': '%d.%m.%Y',
        'mittel': '%d.%m.%Y %H:%M',
        'lang': '%d. %B %Y'
    }
    
    format_string = formate.get(format_typ, formate['kurz'])
    return datum.strftime(format_string)


def tage_bis(zieldatum: datetime) -> int:
    """
    Berechnet die Anzahl Tage bis zu einem Zieldatum.
    
    Args:
        zieldatum: Das Zieldatum
    
    Returns:
        Anzahl Tage (negativ wenn in der Vergangenheit)
    
    Beispiel:
        >>> ziel = datetime(2025, 12, 31)
        >>> tage = tage_bis(ziel)
    """
    heute = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    ziel = zieldatum.replace(hour=0, minute=0, second=0, microsecond=0)
    differenz = ziel - heute
    return differenz.days


def erstelle_passwort_score(passwort: str) -> dict:
    """
    Bewertet die Stärke eines Passworts.
    
    Args:
        passwort: Das zu bewertende Passwort
    
    Returns:
        Dictionary mit Score und Feedback
    
    Beispiel:
        >>> score = erstelle_passwort_score('MeinSicheres123!')
        >>> score['punkte']
        4
    """
    punkte = 0
    feedback = []
    
    # Länge prüfen
    if len(passwort) >= 8:
        punkte += 1
        feedback.append("✓ Ausreichende Länge")
    else:
        feedback.append("✗ Zu kurz (mindestens 8 Zeichen)")
    
    # Kleinbuchstaben
    if re.search(r'[a-z]', passwort):
        punkte += 1
        feedback.append("✓ Enthält Kleinbuchstaben")
    else:
        feedback.append("✗ Keine Kleinbuchstaben")
    
    # Großbuchstaben
    if re.search(r'[A-Z]', passwort):
        punkte += 1
        feedback.append("✓ Enthält Großbuchstaben")
    else:
        feedback.append("✗ Keine Großbuchstaben")
    
    # Zahlen
    if re.search(r'\d', passwort):
        punkte += 1
        feedback.append("✓ Enthält Zahlen")
    else:
        feedback.append("✗ Keine Zahlen")
    
    # Sonderzeichen
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', passwort):
        punkte += 1
        feedback.append("✓ Enthält Sonderzeichen")
    else:
        feedback.append("✗ Keine Sonderzeichen")
    
    # Bewertung
    if punkte >= 5:
        staerke = "Sehr stark"
    elif punkte >= 4:
        staerke = "Stark"
    elif punkte >= 3:
        staerke = "Mittel"
    elif punkte >= 2:
        staerke = "Schwach"
    else:
        staerke = "Sehr schwach"
    
    return {
        'punkte': punkte,
        'maximum': 5,
        'staerke': staerke,
        'feedback': feedback
    }


def bereinige_liste(liste: List[str]) -> List[str]:
    """
    Entfernt Duplikate und leere Einträge aus einer Liste.
    
    Args:
        liste: Die zu bereinigende Liste
    
    Returns:
        Die bereinigte Liste
    
    Beispiel:
        >>> bereinige_liste(['a', 'b', '', 'a', 'c'])
        ['a', 'b', 'c']
    """
    # Entferne leere Strings und behalte Reihenfolge bei
    bereinigte = []
    gesehen = set()
    
    for element in liste:
        element = element.strip()
        if element and element not in gesehen:
            bereinigte.append(element)
            gesehen.add(element)
    
    return bereinigte


def main():
    """Demonstriert die Utility-Funktionen."""
    print("=== Utility-Funktionen Beispiele ===\n")
    
    # E-Mail Validierung
    print("1. E-Mail Validierung:")
    emails = ['max@beispiel.de', 'ungueltig', 'test@test.com']
    for email in emails:
        gueltig = "✓ gültig" if ist_gueltige_email(email) else "✗ ungültig"
        print(f"  {email}: {gueltig}")
    print()
    
    # Telefonnummer formatieren
    print("2. Telefonnummer Formatierung:")
    nummer = '01701234567'
    formatiert = formatiere_telefonnummer(nummer)
    print(f"  {nummer} → {formatiert}\n")
    
    # Text verkürzen
    print("3. Text verkürzen:")
    langer_text = "Dies ist ein sehr langer Text, der verkürzt werden soll"
    print(f"  Original: {langer_text}")
    print(f"  Verkürzt: {verkuerze_text(langer_text, 30)}\n")
    
    # Datum formatieren
    print("4. Datum Formatierung:")
    jetzt = datetime.now()
    print(f"  Kurz: {formatiere_datum(jetzt, 'kurz')}")
    print(f"  Mittel: {formatiere_datum(jetzt, 'mittel')}")
    print(f"  Lang: {formatiere_datum(jetzt, 'lang')}\n")
    
    # Passwort-Stärke
    print("5. Passwort-Stärke:")
    passwoerter = ['123456', 'MeinPasswort', 'Sicher123!']
    for pw in passwoerter:
        score = erstelle_passwort_score(pw)
        print(f"  '{pw}' - {score['staerke']} ({score['punkte']}/{score['maximum']} Punkte)")
    print()
    
    # Liste bereinigen
    print("6. Liste bereinigen:")
    liste = ['Apfel', 'Banane', '', 'Apfel', 'Kirsche', 'Banane']
    print(f"  Original: {liste}")
    print(f"  Bereinigt: {bereinige_liste(liste)}")


if __name__ == "__main__":
    main()
