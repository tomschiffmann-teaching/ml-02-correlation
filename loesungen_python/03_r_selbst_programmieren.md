# Python-Aufgabe 3 · r selbst programmieren

## Aufgabe

Schreibe eine Funktion, die r **genau so berechnet wie du von Hand**, und prüfe sie mit NumPy.

```python
import numpy as np

entfernung = np.array([2, 4, 6, 8, 10])
lieferzeit = np.array([15, 20, 30, 35, 50])

def korrelation(x, y):
    dx = ...          # TODO: Abweichungen von x
    dy = ...          # TODO: Abweichungen von y
    zaehler = ...     # TODO: Summe der Produkte
    nenner = ...      # TODO: Wurzel aus (Summe dx² · Summe dy²)
    return zaehler / nenner

print(f"selbst gerechnet: {korrelation(entfernung, lieferzeit):.3f}")
print(f"mit NumPy:        {np.corrcoef(entfernung, lieferzeit)[0, 1]:.3f}")
```

**a)** Ergänze die Funktion. Beide Ausgaben müssen **0,981** zeigen.
**b)** Prüfe damit deine Ergebnisse aus Aufgabe 3a, 3b und 3c.
**c)** Baue die Kontrolle 1 ein: Lass dir `dx.sum()` und `dy.sum()` ausgeben. Was fällt dir auf?

---

## Lösung

Erzeugt mit `03_r_selbst_programmieren.py` (kein Bild, nur Konsolenausgabe).

## a) Die Funktion

```python
def korrelation(x, y):
    dx = x - x.mean()
    dy = y - y.mean()
    zaehler = np.sum(dx * dy)
    nenner = np.sqrt(np.sum(dx**2) * np.sum(dy**2))
    return zaehler / nenner
```

Ausgabe:

```
selbst gerechnet: 0.981
mit NumPy:        0.981
```

## b) Handrechnungen prüfen

Das Skript druckt für jede Aufgabe genau die Tabelle, die man von Hand anlegt, und am Ende r:

| Aufgabe | x̄ | ȳ | Σ Produkt | Σ (x − x̄)² | Σ (y − ȳ)² | r |
| ------- | -: | -: | --------: | ---------: | ---------: | -----: |
| 3a · Heizkosten | 10 | 28 | −310 | 250 | 392 | **−0,990** |
| 3b · Schlaf und Tippfehler | 7 | 5 | −5 | 10 | 10 | **−0,500** |
| 3c · Wartung und Störungen | 3 | 6 | −17 | 10 | 30 | **−0,981** |

## c) Kontrolle 1

Beide Summen `dx.sum()` und `dy.sum()` sind 0 (bzw. `0.0`). Das ist Kontrolle 1: Die Abweichungen vom Mittelwert heben sich immer auf.
