"""Lösung Python-Aufgabe 6 · 200 Zufallsmerkmale: Eines „passt" immer.

Gehört auch zu Aufgabe 6a Nr. 4 (Wochentag) und Aufgabe 6b Nr. 5 (Regalnummer).
"""
import numpy as np

rng = np.random.default_rng(42)
n_tage, n_merkmale = 20, 200    # e) n_tage auf 200 setzen: die Zufalls-r werden viel kleiner

ziel = rng.normal(size=n_tage)                         # z. B. Tagesumsatz
merkmale = rng.normal(size=(n_tage, n_merkmale))       # 200 zufällige Kennzahlen

# a)
r_werte = np.array([np.corrcoef(merkmale[:, i], ziel)[0, 1] for i in range(n_merkmale)])

# b)
bestes = np.argmax(np.abs(r_werte))
print(f"Bestes Merkmal: Nr. {bestes} mit r = {r_werte[bestes]:+.2f}")

# c)
print(f"Merkmale mit |r| > 0,4: {np.sum(np.abs(r_werte) > 0.4)} von {n_merkmale}")

# d) Neue Daten: Der „Fund" hält nicht
ziel_neu = rng.normal(size=n_tage)
merkmal_neu = rng.normal(size=n_tage)
print(f"Mit neuen Daten: r = {np.corrcoef(merkmal_neu, ziel_neu)[0, 1]:+.2f}")

# e) direkt vergleichen
print("\nGrößtes |r| unter 200 Zufallsmerkmalen, je nach Anzahl Tage:")
for n in (10, 20, 50, 200, 1000):
    z = rng.normal(size=n)
    m = rng.normal(size=(n, n_merkmale))
    groesstes = max(abs(np.corrcoef(m[:, i], z)[0, 1]) for i in range(n_merkmale))
    print(f"  {n:>4} Tage: {groesstes:.2f}")

# f) Regel: Erst die Vermutung, dann die Suche. Einen Fund mit neuen Daten bestätigen.
