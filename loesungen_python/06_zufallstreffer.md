# Python-Aufgabe 6 · Zufallstreffer finden

## Aufgabe

Hier gibt es **nur Zufallszahlen**, also garantiert keinen echten Zusammenhang. Trotzdem wirst du etwas „finden".

```python
import numpy as np

rng = np.random.default_rng(42)
n_tage, n_merkmale = 20, 200

ziel = rng.normal(size=n_tage)                         # z. B. Tagesumsatz
merkmale = rng.normal(size=(n_tage, n_merkmale))       # 200 zufällige Kennzahlen

# TODO a) Für jedes der 200 Merkmale r mit dem Ziel berechnen (Schleife oder Liste)
# TODO b) Das Merkmal mit dem größten |r| finden und ausgeben (np.argmax, np.abs)
# TODO c) Zählen, wie viele Merkmale |r| > 0,4 haben
# TODO d) Neue Zufallsdaten für Ziel und bestes Merkmal ziehen: Wie groß ist r jetzt?
```

**e)** Was passiert, wenn du `n_tage` auf 200 erhöhst? Erkläre.
**f)** Formuliere eine Regel für die Praxis, die man aus diesem Experiment ableiten kann.

---

## Lösung

Erzeugt mit `06_zufallstreffer.py` (kein Bild, nur Konsolenausgabe). Gehört auch zu Aufgabe 6a Nr. 4 (Wochentag) und Aufgabe 6b Nr. 5 (Regalnummer).

## a) bis d) Kernidee im Code

```python
# a)
r_werte = np.array([np.corrcoef(merkmale[:, i], ziel)[0, 1] for i in range(n_merkmale)])

# b)
bestes = np.argmax(np.abs(r_werte))
print(f"Bestes Merkmal: Nr. {bestes} mit r = {r_werte[bestes]:+.2f}")       # ca. -0.65

# c)
print(f"Merkmale mit |r| > 0,4: {np.sum(np.abs(r_werte) > 0.4)}")           # ca. 14

# d)
ziel_neu = rng.normal(size=n_tage)
merkmal_neu = rng.normal(size=n_tage)
print(f"Mit neuen Daten: r = {np.corrcoef(merkmal_neu, ziel_neu)[0, 1]:+.2f}")   # irgendwo um 0
```

Obwohl alle Daten reiner Zufall sind, findet man unter 200 Merkmalen immer eines mit einem scheinbar starken r. Mit neuen Daten verschwindet dieser „Fund“ wieder.

## e) Mehr Tage

Mit 200 Tagen werden die Zufalls-r deutlich kleiner. Je mehr Datenpunkte, desto seltener entsteht rein zufällig ein großes r. Das Skript vergleicht dazu das größte |r| unter 200 Zufallsmerkmalen bei 10, 20, 50, 200 und 1000 Tagen.

## f) Regel für die Praxis

**Erst die Vermutung, dann die Suche.** Wer ohne Hypothese Hunderte Merkmale durchsucht, findet immer etwas. Einen Fund sollte man deshalb mit **neuen Daten** bestätigen, bevor man ihm glaubt.
