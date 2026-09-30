"""Lösung Python-Aufgabe 2 · Punktwolken mit vorgegebenem r erzeugen und schätzen."""
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
ziel_r = [-0.95, -0.5, 0.0, 0.5, 0.95]
n_punkte = 100          # c) auf 10 setzen: das gemessene r schwankt viel stärker
titel_zeigen = True     # b) auf False setzen, dann schätzt die Partnerin oder der Partner

fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for ax, r in zip(axes, ziel_r):
    x = rng.normal(size=n_punkte)
    rauschen = rng.normal(size=n_punkte)
    y = r * x + np.sqrt(1 - r**2) * rauschen
    gemessen = np.corrcoef(x, y)[0, 1]
    ax.scatter(x, y, s=10)
    ax.set_title(f"Ziel {r:+.2f} · gemessen {gemessen:+.2f}" if titel_zeigen else "")
plt.tight_layout()
fig.savefig("02_punktwolken.png", dpi=120)
plt.show()

# c) Wie stark schwankt r bei 10 und bei 100 Punkten? (Ziel r = 0,5, je 1000 Versuche)
for n in (10, 100):
    werte = []
    for _ in range(1000):
        x, rauschen = rng.normal(size=n), rng.normal(size=n)
        werte.append(np.corrcoef(x, 0.5 * x + np.sqrt(0.75) * rauschen)[0, 1])
    print(f"n = {n:>3}: gemessenes r liegt meist zwischen "
          f"{np.percentile(werte, 5):+.2f} und {np.percentile(werte, 95):+.2f}")
