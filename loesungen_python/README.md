# 🐍 Musterlösungen · Python-Aufgaben zum Skript „Korrelation“ (DA-02.2)

Eine Datei pro Python-Aufgabe im Skript. Alle Beispiele stammen aus dem Skript.

| Datei | Aufgabe im Skript | Zeigt |
|---|---|---|
| `02_punktwolken.py` | Python-Aufgabe 2 | Daten mit vorgegebenem r erzeugen, Schwankung bei 10 vs. 100 Punkten |
| `03_r_selbst_programmieren.py` | Python-Aufgabe 3 + Kontrolle von **Aufgabe 3a, 3b, 3c** | r wie von Hand, druckt die komplette Rechentabelle |
| `04_r_und_steigung.py` | Python-Aufgabe 4 | Maschinen A/B/C: gleiches \|r\|, verschiedene Steigung |
| `05_bogen_und_ausreisser.py` | Python-Aufgabe 5 (+ Aufgabe 5 Café) | Bogen → r ≈ 0, Ausreißer → r springt |
| `06_zufallstreffer.py` | Python-Aufgabe 6 (+ Aufgabe 6a Nr. 4, 6b Nr. 5) | 200 Zufallsmerkmale, eines „passt“ immer |
| `08_stoervariable_entlarven.py` | Python-Aufgabe 8 (+ Laptop-Beispiel aus Kapitel 6) | Störvariable Temperatur bzw. Kaufjahr mit Weg ③ entlarven |

## Ausführen

```bash
cd ~/Desktop/ML/loesungen_python
python3 -m venv .venv
source .venv/bin/activate          # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python 03_r_selbst_programmieren.py
```

Aufräumen: `deactivate` und danach den Ordner `.venv` löschen.
