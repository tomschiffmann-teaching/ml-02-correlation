"""Lösung Python-Aufgabe 3 · r selbst programmieren und die Handrechnungen 3a bis 3c prüfen."""
import numpy as np

entfernung = np.array([2, 4, 6, 8, 10])
lieferzeit = np.array([15, 20, 30, 35, 50])


def korrelation(x, y):
    dx = x - x.mean()
    dy = y - y.mean()
    zaehler = np.sum(dx * dy)
    nenner = np.sqrt(np.sum(dx**2) * np.sum(dy**2))
    return zaehler / nenner


# a)
print(f"selbst gerechnet: {korrelation(entfernung, lieferzeit):.3f}")
print(f"mit NumPy:        {np.corrcoef(entfernung, lieferzeit)[0, 1]:.3f}")


def tabelle(name, x, y):
    """Druckt genau die Tabelle, die man von Hand anlegt."""
    x, y = np.asarray(x, dtype=float), np.asarray(y, dtype=float)
    dx, dy = x - x.mean(), y - y.mean()
    print(f"\n── {name} ──  x̄ = {x.mean():g}   ȳ = {y.mean():g}")
    print(f"{'x':>5} {'y':>5} {'x−x̄':>6} {'y−ȳ':>6} {'Produkt':>8} {'(x−x̄)²':>8} {'(y−ȳ)²':>8}")
    for xi, yi, a, b in zip(x, y, dx, dy):
        print(f"{xi:>5g} {yi:>5g} {a:>+6g} {b:>+6g} {a * b + 0:>8g} {a**2:>8g} {b**2:>8g}")
    print(f"{'Σ':>5} {'':>5} {dx.sum():>+6g} {dy.sum():>+6g} {np.sum(dx * dy):>8g} "
          f"{np.sum(dx**2):>8g} {np.sum(dy**2):>8g}")
    # c) Kontrolle 1: Die Abweichungen summieren sich immer zu 0
    print(f"Kontrolle 1: Σ dx = {dx.sum():g}, Σ dy = {dy.sum():g}")
    print(f"r = {korrelation(x, y):+.3f}   (NumPy: {np.corrcoef(x, y)[0, 1]:+.3f})")


# b) Handrechnungen prüfen
tabelle("Aufgabe 3a · Heizkosten", [0, 5, 10, 15, 20], [40, 34, 30, 20, 16])
tabelle("Aufgabe 3b · Schlaf und Tippfehler", [5, 6, 7, 8, 9], [6, 7, 3, 4, 5])
tabelle("Aufgabe 3c · Wartung und Störungen", [1, 2, 3, 4, 5], [9, 8, 6, 5, 2])
