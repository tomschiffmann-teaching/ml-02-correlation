"""Lösung Python-Aufgabe 4 · Gleiches r, ganz verschiedene Steigung."""
import numpy as np
import matplotlib.pyplot as plt

stufe = np.array([1, 2, 3, 4, 5])
temp_a = np.array([10, 12, 11, 13, 14])
temp_b = np.array([10, 30, 20, 40, 50])
# b) Gleiches |r| mit negativer Steigung: B spiegeln. r wird dann aber auch negativ,
#    denn Vorzeichen von r und Vorzeichen der Steigung sind immer gleich.
temp_c = 60 - temp_b

maschinen = [("A", temp_a), ("B", temp_b), ("C", temp_c)]

# a)
for name, y in maschinen:
    r = np.corrcoef(stufe, y)[0, 1]
    steigung, achsenabschnitt = np.polyfit(stufe, y, 1)
    print(f"Maschine {name}: r = {r:+.2f}, Steigung = {steigung:+.1f} °C pro Stufe")

# c)
for name, y in maschinen:
    plt.scatter(stufe, y, label=f"Maschine {name}")
    steigung, achsenabschnitt = np.polyfit(stufe, y, 1)
    plt.plot(stufe, steigung * stufe + achsenabschnitt, linestyle="--")
plt.xlabel("Drehzahlstufe")
plt.ylabel("Temperaturerhöhung (°C)")
plt.title("Gleiches |r| = 0,90, aber sehr unterschiedliche Wirkung")
plt.legend()
plt.savefig("04_r_und_steigung.png", dpi=120)
plt.show()
