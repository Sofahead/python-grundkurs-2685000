"""
Modul mit Klassen-Beispielen und objektorientierten Best Practices.

Dieses Modul demonstriert:
- Klassen und Objekte
- Eigenschaften und Methoden
- Datenkapselung (private Attribute)
- __str__ und __repr__ Methoden
- Property Decorators
"""

from datetime import datetime
from typing import List


class Buch:
    """
    Repräsentiert ein Buch mit Titel, Autor und Erscheinungsjahr.
    
    Attributes:
        titel: Der Titel des Buches
        autor: Der Autor des Buches
        jahr: Das Erscheinungsjahr
    """
    
    def __init__(self, titel: str, autor: str, jahr: int):
        """
        Initialisiert ein neues Buch.
        
        Args:
            titel: Der Titel des Buches
            autor: Der Autor des Buches
            jahr: Das Erscheinungsjahr
        """
        self.titel = titel
        self.autor = autor
        self.jahr = jahr
    
    def alter(self) -> int:
        """
        Berechnet das Alter des Buches.
        
        Returns:
            Die Anzahl Jahre seit Erscheinung
        """
        aktuelles_jahr = datetime.now().year
        return aktuelles_jahr - self.jahr
    
    def __str__(self) -> str:
        """Gibt eine lesbare String-Darstellung zurück."""
        return f'"{self.titel}" von {self.autor} ({self.jahr})'
    
    def __repr__(self) -> str:
        """Gibt eine technische String-Darstellung zurück."""
        return f'Buch(titel="{self.titel}", autor="{self.autor}", jahr={self.jahr})'


class Bibliothek:
    """
    Verwaltet eine Sammlung von Büchern.
    
    Attributes:
        name: Der Name der Bibliothek
    """
    
    def __init__(self, name: str):
        """
        Initialisiert eine neue Bibliothek.
        
        Args:
            name: Der Name der Bibliothek
        """
        self.name = name
        self._buecher: List[Buch] = []  # Private Liste
    
    def buch_hinzufuegen(self, buch: Buch) -> None:
        """
        Fügt ein Buch zur Bibliothek hinzu.
        
        Args:
            buch: Das hinzuzufügende Buch
        """
        self._buecher.append(buch)
        print(f'✓ Buch hinzugefügt: {buch.titel}')
    
    def anzahl_buecher(self) -> int:
        """
        Gibt die Anzahl der Bücher in der Bibliothek zurück.
        
        Returns:
            Die Anzahl der Bücher
        """
        return len(self._buecher)
    
    def finde_nach_autor(self, autor: str) -> List[Buch]:
        """
        Findet alle Bücher eines bestimmten Autors.
        
        Args:
            autor: Der gesuchte Autor
        
        Returns:
            Liste der gefundenen Bücher
        """
        return [buch for buch in self._buecher if buch.autor.lower() == autor.lower()]
    
    def aelteste_buecher(self, anzahl: int = 5) -> List[Buch]:
        """
        Gibt die ältesten Bücher der Bibliothek zurück.
        
        Args:
            anzahl: Wie viele Bücher zurückgegeben werden sollen
        
        Returns:
            Liste der ältesten Bücher
        """
        return sorted(self._buecher, key=lambda b: b.jahr)[:anzahl]
    
    def __str__(self) -> str:
        """Gibt eine lesbare String-Darstellung zurück."""
        return f'Bibliothek "{self.name}" mit {self.anzahl_buecher()} Büchern'


class BankKonto:
    """
    Repräsentiert ein Bankkonto mit Kontostand und Transaktionen.
    
    Demonstriert Datenkapselung und Property Decorators.
    """
    
    def __init__(self, kontoinhaber: str, anfangssaldo: float = 0.0):
        """
        Initialisiert ein neues Bankkonto.
        
        Args:
            kontoinhaber: Name des Kontoinhabers
            anfangssaldo: Anfänglicher Kontostand (Standard: 0.0)
        """
        self.kontoinhaber = kontoinhaber
        self._saldo = anfangssaldo  # Private Variable
        self._transaktionen: List[str] = []
    
    @property
    def saldo(self) -> float:
        """
        Gibt den aktuellen Kontostand zurück.
        
        Returns:
            Der aktuelle Saldo
        """
        return self._saldo
    
    def einzahlen(self, betrag: float) -> bool:
        """
        Zahlt einen Betrag auf das Konto ein.
        
        Args:
            betrag: Der einzuzahlende Betrag
        
        Returns:
            True bei Erfolg, False bei ungültigem Betrag
        """
        if betrag <= 0:
            print("Fehler: Betrag muss positiv sein")
            return False
        
        self._saldo += betrag
        self._transaktionen.append(f"Einzahlung: +{betrag:.2f}€")
        print(f"✓ {betrag:.2f}€ eingezahlt. Neuer Saldo: {self._saldo:.2f}€")
        return True
    
    def abheben(self, betrag: float) -> bool:
        """
        Hebt einen Betrag vom Konto ab.
        
        Args:
            betrag: Der abzuhebende Betrag
        
        Returns:
            True bei Erfolg, False bei Fehler
        """
        if betrag <= 0:
            print("Fehler: Betrag muss positiv sein")
            return False
        
        if betrag > self._saldo:
            print("Fehler: Unzureichender Kontostand")
            return False
        
        self._saldo -= betrag
        self._transaktionen.append(f"Abhebung: -{betrag:.2f}€")
        print(f"✓ {betrag:.2f}€ abgehoben. Neuer Saldo: {self._saldo:.2f}€")
        return True
    
    def transaktionsverlauf(self) -> List[str]:
        """
        Gibt den vollständigen Transaktionsverlauf zurück.
        
        Returns:
            Liste aller Transaktionen
        """
        return self._transaktionen.copy()
    
    def __str__(self) -> str:
        """Gibt eine lesbare String-Darstellung zurück."""
        return f'Konto von {self.kontoinhaber}: {self._saldo:.2f}€'


def main():
    """Demonstriert die Verwendung der Klassen."""
    print("=== Klassen-Beispiele ===\n")
    
    # Bibliothek erstellen
    print("1. Bibliothek-Verwaltung:")
    print("-" * 40)
    bibliothek = Bibliothek("Stadtbibliothek")
    
    # Bücher hinzufügen
    buch1 = Buch("Python für Einsteiger", "Dr. Julia Imlauer", 2023)
    buch2 = Buch("Clean Code", "Robert C. Martin", 2008)
    buch3 = Buch("Design Patterns", "Gang of Four", 1994)
    
    bibliothek.buch_hinzufuegen(buch1)
    bibliothek.buch_hinzufuegen(buch2)
    bibliothek.buch_hinzufuegen(buch3)
    
    print(f"\n{bibliothek}")
    print(f"Ältestes Buch: {bibliothek.aelteste_buecher(1)[0]}")
    print(f"Alter des Buches: {buch1.alter()} Jahre\n")
    
    # Bankkonto demonstrieren
    print("2. Bankkonto-Verwaltung:")
    print("-" * 40)
    konto = BankKonto("Max Mustermann", 1000.0)
    print(f"Neues Konto: {konto}\n")
    
    konto.einzahlen(500.0)
    konto.abheben(200.0)
    konto.abheben(2000.0)  # Sollte fehlschlagen
    
    print(f"\nAktueller Stand: {konto}")
    print("\nTransaktionsverlauf:")
    for transaktion in konto.transaktionsverlauf():
        print(f"  • {transaktion}")


if __name__ == "__main__":
    main()
