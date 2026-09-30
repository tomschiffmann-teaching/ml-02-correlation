"""Lösung Python-Aufgabe 5 · Bogen und Ausreißer: erst schauen, dann rechnen."""
import numpy as np
import matplotlib.pyplot as plt

# Teil 1: Bogen
rng = np.random.default_rng(1)
raumtemp = np.linspace(14, 28, 40)
konzentration = 90 - 1.2 * (raumtemp - 21) ** 2 + rng.normal(0, 3, 40)

# a)
r_gesamt = np.corrcoef(raumtemp, konzentration)[0, 1]
print(f"r gesamt:     {r_gesamt:+.2f}")

# b)
kalt = raumtemp <= 21
warm = raumtemp > 21
print(f"r bis 21 °C:  {np.corrcoef(raumtemp[kalt], konzentration[kalt])[0, 1]:+.2f}")
print(f"r über 21 °C: {np.corrcoef(raumtemp[warm], konzentration[warm])[0, 1]:+.2f}")

# Teil 2: Ausreißer
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 2, 4, 3])

# d)
print(f"\nohne Ausreißer: r = {np.corrcoef(x, y)[0, 1]:+.2f}")
x_neu, y_neu = np.append(x, 12), np.append(y, 12)
print(f"mit Ausreißer:  r = {np.corrcoef(x_neu, y_neu)[0, 1]:+.2f}")

# Zusatz: Aufgabe 5 (Café) nachrechnen
sonne = np.array([0, 2, 4, 6, 8])
getraenke = np.array([50, 80, 90, 80, 50])
print(f"\nAufgabe 5 · Café: r = {np.corrcoef(sonne, getraenke)[0, 1]:+.2f}")

# c) Streudiagramme
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.scatter(raumtemp[kalt], konzentration[kalt], label="bis 21 °C")
ax1.scatter(raumtemp[warm], konzentration[warm], label="über 21 °C")
ax1.set_xlabel("Raumtemperatur (°C)")
ax1.set_ylabel("Konzentration (Punkte)")
ax1.set_title(f"Bogen: r gesamt = {r_gesamt:+.2f}")
ax1.legend()

ax2.scatter(x, y, label="5 normale Punkte")
ax2.scatter([12], [12], color="red", label="Ausreißer (12|12)")
ax2.set_title(f"Ausreißer: r springt auf {np.corrcoef(x_neu, y_neu)[0, 1]:+.2f}")
ax2.legend()
fig.tight_layout()
fig.savefig("05_bogen_und_ausreisser.png", dpi=120)
plt.show()
