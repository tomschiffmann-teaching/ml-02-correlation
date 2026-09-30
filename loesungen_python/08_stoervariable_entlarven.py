"""Lösung Python-Aufgabe 8 · Eine Störvariable entlarven (Weg ③: vergleichbare Fälle vergleichen)."""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
n = 3650
temperatur = rng.uniform(0, 35, n)                           # die Störvariable
eis = 20 + 8 * temperatur + rng.normal(0, 30, n)             # hängt NUR von der Temperatur ab
sonnenbrand = 1 + 0.4 * temperatur + rng.normal(0, 2, n)     # hängt NUR von der Temperatur ab

df = pd.DataFrame({"temperatur": temperatur, "eis": eis, "sonnenbrand": sonnenbrand})

# a)
print(df[["temperatur", "eis", "sonnenbrand"]].corr().round(2))

# b)
df["temp_klasse"] = pd.cut(df["temperatur"], bins=range(0, 36, 1))

# c)
werte = []
for klasse, gruppe in df.groupby("temp_klasse", observed=True):
    werte.append(gruppe["eis"].corr(gruppe["sonnenbrand"]))
print(f"\nr insgesamt:                             {df['eis'].corr(df['sonnenbrand']):+.2f}")
print(f"r bei gleicher Temperatur (Durchschnitt): {np.mean(werte):+.2f}")

# d) Insgesamt stark, bei gleicher Temperatur ≈ 0 → die Temperatur ist die Störvariable.

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.scatter(df["eis"], df["sonnenbrand"], s=3, alpha=0.3)
ax1.set_title("Alle Tage: Eis und Sonnenbrand hängen „zusammen“")
ax1.set_xlabel("Eisverkauf")
ax1.set_ylabel("Sonnenbrände")
gleich = df[(df["temperatur"] >= 25) & (df["temperatur"] < 26)]
ax2.scatter(gleich["eis"], gleich["sonnenbrand"], s=10)
ax2.set_title("Nur Tage mit 25–26 °C: kein Zusammenhang")
ax2.set_xlabel("Eisverkauf")
fig.tight_layout()
fig.savefig("08_stoervariable_entlarven.png", dpi=120)
plt.show()

# e) Übertragen auf das Laptop-Beispiel aus Kapitel 6:
#    Schwarze Laptops gibt es erst seit zwei Jahren, jüngere Laptops gehen seltener kaputt.
#    Die Farbe selbst wirkt NICHT, nur das Kaufjahr steckt in der Formel.
n = 20_000
kaufjahr = rng.integers(2019, 2027, n)
schwarz = np.where(kaufjahr >= 2025, rng.random(n) < 0.8, rng.random(n) < 0.1)
alter = 2026 - kaufjahr
defekt = rng.random(n) < 0.03 + 0.03 * alter
laptops = pd.DataFrame({
    "kaufjahr": kaufjahr,
    "farbe": np.where(schwarz, "schwarz", "silber"),
    "defekt": defekt,
})

print("\nLaptops · Defektrate nach Farbe (alle zusammen):")
print(laptops.groupby("farbe")["defekt"].mean().round(3))
print("\nLaptops · Defektrate nach Kaufjahr UND Farbe (Weg ③):")
print(laptops.groupby(["kaufjahr", "farbe"])["defekt"].mean().unstack().round(3))
