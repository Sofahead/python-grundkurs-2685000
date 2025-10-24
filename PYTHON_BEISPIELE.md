# Python Best Practices - Beispielcode

Dieser Code demonstriert Best Practices für Python-Entwicklung im Rahmen des Python Grundkurses.

## 📚 Übersicht

Dieses Repository enthält gut strukturierten, dokumentierten Python-Code, der folgende Best Practices demonstriert:

### Module

1. **calculator.py** - Taschenrechner-Modul
   - Grundlegende mathematische Operationen
   - Type Hints für Typsicherheit
   - Fehlerbehandlung (z.B. Division durch Null)
   - Umfassende Docstrings

2. **daten_verarbeitung.py** - Datenverarbeitung
   - Listen und Dictionary-Operationen
   - List Comprehensions
   - Funktionale Programmierung
   - Statistische Auswertungen

3. **datei_operationen.py** - Dateioperationen
   - Sichere Datei-I/O mit Context Managern
   - JSON-Verarbeitung
   - Fehlerbehandlung für I/O-Operationen
   - Pathlib für Pfad-Handling

4. **klassen_beispiel.py** - Objektorientierte Programmierung
   - Klassen und Objekte
   - Datenkapselung (private Attribute)
   - Property Decorators
   - `__str__` und `__repr__` Methoden

5. **utilities.py** - Hilfsfunktionen
   - String-Manipulation
   - Validierung (E-Mail, Passwörter)
   - Datum/Zeit-Funktionen
   - Reguläre Ausdrücke

6. **hauptprogramm.py** - Hauptanwendung
   - Integration aller Module
   - Interaktiver und automatischer Modus
   - Strukturierte Programmorganisation

## 🚀 Verwendung

### Einzelne Module ausführen

Jedes Modul kann eigenständig ausgeführt werden:

```bash
python calculator.py
python daten_verarbeitung.py
python datei_operationen.py
python klassen_beispiel.py
python utilities.py
```

### Hauptprogramm (alle Demos)

Für eine interaktive Demo aller Module:

```bash
python hauptprogramm.py
```

Im automatischen Modus (z.B. für CI/CD):

```bash
python hauptprogramm.py < /dev/null
```

## ✨ Best Practices demonstriert

### 1. Code-Struktur
- ✅ Aussagekräftige Namen für Funktionen und Variablen
- ✅ Modulare Organisation
- ✅ Separation of Concerns (ein Modul = eine Verantwortlichkeit)

### 2. Dokumentation
- ✅ Docstrings im Google-Style für alle Module, Klassen und Funktionen
- ✅ Type Hints für bessere Lesbarkeit und IDE-Unterstützung
- ✅ Inline-Kommentare wo sinnvoll

### 3. Fehlerbehandlung
- ✅ Try-Except-Blöcke für I/O-Operationen
- ✅ Validierung von Eingabedaten
- ✅ Aussagekräftige Fehlermeldungen

### 4. Objektorientierung
- ✅ Klassen für zusammengehörige Daten und Verhalten
- ✅ Datenkapselung mit privaten Attributen (`_attribut`)
- ✅ Properties für kontrollierten Zugriff auf Daten

### 5. PEP 8 Konformität
- ✅ 4 Leerzeichen für Einrückung
- ✅ Konsistente Namenskonventionen:
  - `snake_case` für Funktionen und Variablen
  - `PascalCase` für Klassen
  - `UPPER_CASE` für Konstanten (wo verwendet)
- ✅ Sinnvolle Zeilenlängen

### 6. Pythonic Code
- ✅ List Comprehensions statt expliziter Schleifen
- ✅ Context Manager (`with`) für Ressourcen
- ✅ `if __name__ == "__main__":` Pattern
- ✅ Verwendung von Built-in-Funktionen

## 🎯 Lernziele

Nach dem Studium dieses Codes sollten Sie verstehen:

1. Wie man Python-Code sauber und wartbar strukturiert
2. Wie man aussagekräftige Dokumentation schreibt
3. Wie man Fehler angemessen behandelt
4. Wie man objektorientierte Prinzipien in Python anwendet
5. Wie man Type Hints effektiv einsetzt
6. Wie man PEP 8 Richtlinien befolgt

## 📖 Weiterführende Ressourcen

- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [PEP 257 - Docstring Conventions](https://www.python.org/dev/peps/pep-0257/)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [Python Documentation](https://docs.python.org/3/)

## 🔧 Anforderungen

- Python 3.7 oder höher
- Keine externen Abhängigkeiten erforderlich (verwendet nur Standard-Bibliothek)

## 📝 Hinweise

- Alle Beispiele verwenden deutsche Bezeichner, um die Lesbarkeit für deutschsprachige Lernende zu verbessern
- Der Code ist bewusst ausführlich dokumentiert für Lehrzwecke
- Jedes Modul enthält eine `main()` Funktion mit Beispielen
- Die Beispiele sind darauf ausgelegt, schrittweise aufeinander aufzubauen

## 👥 Für Lehrende

Dieser Code eignet sich hervorragend für:
- Code-Reviews im Unterricht
- Diskussion über Best Practices
- Demonstration von Python-Features
- Basis für Übungsaufgaben

## 🤝 Beitragen

Dieses Repository ist Teil eines LinkedIn Learning Kurses. Weitere Informationen finden Sie in der Haupt-README.md.
