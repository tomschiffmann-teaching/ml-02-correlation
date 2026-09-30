# 📈 Korrelation: Wie eng hängen zwei Dinge zusammen?

> **Block DA · Einheit DA-02.2** · Skript für Teilnehmende
>
> So ist jedes Kapitel aufgebaut:
> 📖 **Erklärung** → 🧮 **Rechenbeispiel** → ✏️ **Aufgabe von Hand** → 🐍 **Python-Aufgabe**
>
> Alle Lösungen stehen gesammelt am Ende.

---

## Inhalt

1. [Worum es heute geht](#1--worum-es-heute-geht)
2. [Die Skala von −1 bis +1](#2--die-skala-von-1-bis-1)
3. [r von Hand berechnen](#3--r-von-hand-berechnen)
4. [Grenze 1: r ist nicht die Steigung](#4--grenze-1-r-ist-nicht-die-steigung)
5. [Grenze 2: r = 0 heißt nicht „kein Zusammenhang"](#5--grenze-2-r--0-heißt-nicht-kein-zusammenhang)
6. [Vier Erklärungen für eine Korrelation](#6--vier-erklärungen-für-eine-korrelation)
7. [Vorhersagen oder entscheiden?](#7--vorhersagen-oder-entscheiden)
8. [Wie man Kausalität prüft](#8--wie-man-kausalität-prüft)
9. [Das Wichtigste auf einen Blick](#9--das-wichtigste-auf-einen-blick)
10. [Lösungen](#lösungen)

### Vorbereitung für die Python-Aufgaben

```bash
cd <wo-auch-immer-eure-requirements.txt-liegt>
python3 -m venv .venv
source .venv/bin/activate          # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

> 🐍 Musterlösungen als lauffähige Skripte liegen im Ordner `loesungen_python/`: eine Datei pro Python-Aufgabe.

---

## 1 · Worum es heute geht

### 📖 Erklärung

In der letzten Einheit habt ihr Streudiagramme gezeichnet und mit dem Auge beurteilt: _Steigt die Punktwolke? Fällt sie? Oder ist da gar nichts?_

Das Auge ist gut, aber ungenau. Zwei Leute schauen auf dasselbe Diagramm, und die eine sagt „deutlicher Zusammenhang", der andere „na ja, eher schwach". Wir brauchen also **eine Zahl**, die jeder gleich berechnet und gleich versteht. Diese Zahl heißt **Korrelationskoeffizient r**.

Heute lernt ihr zwei Dinge:

1. **r berechnen und in Worte fassen.** Das ist Handwerk, das habt ihr nach einer Stunde drauf.
2. **r richtig deuten.** Das ist der schwierigere Teil. Eine Korrelation verrät, _dass_ zwei Dinge zusammen auftreten. Sie verrät **nicht**, _warum_. Genau hier passieren in der Praxis die teuersten Fehler.

> 💬 **Ein Gedanke zum Einstieg:** Ein Online-Shop stellt fest, dass Kunden mit Premium-Kreditkarte im Schnitt doppelt so viel bestellen. Sollte der Shop allen Kunden eine Premium-Kreditkarte schenken? Behalte deine Antwort im Kopf. In Kapitel 7 kommen wir darauf zurück.

---

## 2 · Die Skala von −1 bis +1

### 📖 Erklärung

r ist immer eine Zahl zwischen **−1** und **+1**. Sie beantwortet zwei Fragen auf einmal:

| Frage                                           | Woran man es sieht                   |                                                                                 |
| ----------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------- |
| **In welche Richtung** hängen x und y zusammen? | am **Vorzeichen**                    | **+** heißt „je mehr x, desto mehr y", **−** heißt „je mehr x, desto weniger y" |
| **Wie eng** liegen die Punkte an einer Geraden? | am **Betrag** (Zahl ohne Vorzeichen) | nahe 1 heißt eng, nahe 0 heißt lose oder gar nicht                              |

```
   −1 ──────── −0,7 ──── −0,3 ──── 0 ──── +0,3 ──── +0,7 ──────── +1
   │   stark     │ mittel  │ schwach │ schwach │ mittel  │   stark    │
   │ gegenläufig │         │  bzw. kein linearer Zus.  │         │ gleichläufig│

    ╲                               · · ·                              ╱
     ╲  alle Punkte auf einer       · · ·    keine Richtung           ╱  alle Punkte auf einer
      ╲ fallenden Geraden           · · ·                            ╱   steigenden Geraden
```

| Wert von r        | So beschreibst du es                      | So sieht die Punktwolke aus                    |
| ----------------- | ----------------------------------------- | ---------------------------------------------- |
| **+1**            | perfekter gleichläufiger Zusammenhang     | alle Punkte exakt auf einer steigenden Geraden |
| **+0,7 bis +1**   | starker gleichläufiger Zusammenhang       | deutlich steigend, wenig Streuung              |
| **+0,3 bis +0,7** | mittlerer gleichläufiger Zusammenhang     | Tendenz nach oben, aber breite Streuung        |
| **−0,3 bis +0,3** | schwacher bzw. kein linearer Zusammenhang | keine erkennbare Richtung                      |
| **−0,7 bis −0,3** | mittlerer gegenläufiger Zusammenhang      | Tendenz nach unten, breite Streuung            |
| **−1 bis −0,7**   | starker gegenläufiger Zusammenhang        | deutlich fallend, wenig Streuung               |

> 📌 **Merksatz:** Das **Vorzeichen** sagt die **Richtung**, der **Betrag** sagt die **Stärke**.

Die Grenzen 0,3 und 0,7 sind eine **Faustregel**. In der Physik wäre r = 0,9 eine eher enttäuschende Messung, in der Psychologie ein Traumergebnis. Was „stark" ist, hängt vom Fachgebiet ab:

- **Physik:** Hier hängen Größen über feste Gesetze zusammen, etwa Spannung und Stromstärke beim ohmschen Gesetz (U = R · I). Störeinflüsse lassen sich im Labor weitgehend ausschalten, und die Messgeräte sind sehr genau. Man erwartet daher r = 0,99 oder mehr. Ein r von nur 0,9 heißt hier: Irgendetwas stimmt nicht, zum Beispiel das Messgerät, der Versuchsaufbau oder eine unbeachtete Einflussgröße.
- **Psychologie:** Hier geht es um Menschen, zum Beispiel um den Zusammenhang zwischen Lernzeit und Prüfungsnote. Auf die Note wirken viele weitere Dinge: Vorwissen, Schlaf, Nervosität, Tagesform. Außerdem lassen sich Größen wie Motivation oder Zufriedenheit nur ungenau messen, meist mit Fragebögen. Jeder dieser Einflüsse streut die Punktwolke. Deshalb gilt hier schon r = 0,3 bis 0,5 als ordentliches Ergebnis, und r = 0,9 kommt fast nie vor.

> 💡 **Faustregel:** Je mehr unkontrollierte Einflüsse und je ungenauer die Messung, desto niedriger fällt r aus, auch wenn der Zusammenhang echt ist. Betriebliche Daten wie Kundenverhalten oder Mitarbeiterzufriedenheit liegen meist näher an der Psychologie als an der Physik.

### 🧮 Beispiel

| Situation                             |     r | In Worten                                                                              |
| ------------------------------------- | ----: | -------------------------------------------------------------------------------------- |
| Entfernung zum Kunden ↔ Lieferzeit    | +0,98 | starker gleichläufiger Zusammenhang: Je weiter weg, desto länger dauert die Lieferung. |
| Außentemperatur ↔ Heizkosten          | −0,99 | starker gegenläufiger Zusammenhang: Je wärmer, desto niedriger die Heizkosten.         |
| Schuhgröße ↔ Gehalt (bei Erwachsenen) | +0,05 | kein linearer Zusammenhang.                                                            |

### ✏️ Aufgabe 2 · r in Worte fassen

Formuliere für jeden Wert einen vollständigen Satz mit **Richtung**, **Stärke** und **Bedeutung im Kontext**:

1. Trainingsstunden pro Woche ↔ Laufzeit über 10 km: **r = −0,82**
2. Anzahl Mitarbeitende im Laden ↔ Wartezeit an der Kasse: **r = −0,45**
3. Werbebudget ↔ Umsatz: **r = +0,63**
4. Hausnummer ↔ Stromverbrauch: **r = +0,02**

### 🐍 Python-Aufgabe 2 · Punktwolken erzeugen und schätzen

Mit dem folgenden Trick kannst du Daten mit einem **vorgegebenen r** erzeugen:
`y = r · x + √(1 − r²) · Rauschen`

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng()
ziel_r = [-0.95, -0.5, 0.0, 0.5, 0.95]

fig, axes = plt.subplots(1, 5, figsize=(15, 3))
for ax, r in zip(axes, ziel_r):
    x = rng.normal(size=100)
    rauschen = rng.normal(size=100)
    y = ...                  # TODO: Formel von oben einsetzen
    gemessen = ...           # TODO: r mit np.corrcoef(x, y)[0, 1] messen
    ax.scatter(x, y, s=10)
    ax.set_title(f"Ziel {r:+.2f} · gemessen {gemessen:+.2f}")
plt.tight_layout()
plt.show()
```

**a)** Ergänze die beiden `TODO`-Zeilen und führe das Skript aus.
**b)** Tausche mit einer Partnerin oder einem Partner: Die eine Person ändert `ziel_r` heimlich und blendet die Titel aus (`ax.set_title("")`), die andere schätzt r.
**c)** Warum weicht das gemessene r leicht vom Ziel ab? Was passiert, wenn du statt 100 nur 10 Punkte erzeugst?

---

## 3 · r von Hand berechnen

### 📖 Erklärung

Die Formel sieht auf den ersten Blick einschüchternd aus:

$$
r = \frac{\sum (x-\bar{x})(y-\bar{y})}{\sqrt{\sum (x-\bar{x})^2 \cdot \sum (y-\bar{y})^2}}
$$

Sie besteht aber nur aus **drei Summen**, und die Idee dahinter ist einfach.

**Die Idee:** Wir legen ein Kreuz durch den Mittelpunkt der Punktwolke (x̄ | ȳ). Dann fragen wir für jeden Punkt: _Liegt er bei x und y auf derselben Seite des Mittelwerts?_

```
                 senkrechte Linie: x = x̄
                      │
   links oben         │   rechts oben
   x unter Ø          │   x über Ø
   y über Ø           │   y über Ø       •
   Produkt −          │   Produkt +    •
 ─────────────────────●───────────────────── waagerechte Linie: y = ȳ
          •           │
        •             │   ● = Mittelpunkt (x̄ | ȳ)
   x unter Ø          │   x über Ø
   y unter Ø          │   y unter Ø
   Produkt +          │   Produkt −
   links unten        │   rechts unten
```

> ℹ️ Das Kreuz sind **nicht** die normalen Achsen durch 0, sondern zwei Linien durch die **Mittelwerte**. x̄ („x quer“) ist der Mittelwert aller x-Werte, ȳ der Mittelwert aller y-Werte.

- Punkt **rechts oben** oder **links unten**: beide Abweichungen haben dasselbe Vorzeichen, das **Produkt ist positiv**.
- Punkt **links oben** oder **rechts unten**: die Vorzeichen sind verschieden, das **Produkt ist negativ**.

Der **Zähler** addiert alle diese Produkte. Überwiegen die positiven, steigt die Wolke. Überwiegen die negativen, fällt sie. Heben sie sich auf, gibt es keine Richtung.

Der **Nenner** sorgt nur dafür, dass am Ende eine Zahl zwischen −1 und +1 herauskommt, egal ob wir in Metern, Euro oder Minuten messen. Deshalb hat **r keine Einheit**.

> 💡 Die Tabelle kennt ihr schon von der Ausgleichsgeraden. Es kommt nur **eine Spalte** dazu: (y − ȳ)².

### 🧮 Rechenbeispiel · Lieferdienst

Ein Lieferdienst notiert für fünf Bestellungen die **Entfernung x (km)** und die **Lieferzeit y (min)**.

**Schritt 1 · Mittelwerte**

x̄ = (2 + 4 + 6 + 8 + 10) / 5 = 30 / 5 = **6**
ȳ = (15 + 20 + 30 + 35 + 50) / 5 = 150 / 5 = **30**

**Schritt 2 bis 3 · Tabelle füllen**

| Bestellung |      x |       y |   x − x̄ |   y − ȳ | (x − x̄)(y − ȳ) | (x − x̄)² | (y − ȳ)² |
| ---------- | -----: | ------: | ------: | ------: | -------------: | -------: | -------: |
| 1          |      2 |      15 |      −4 |     −15 |             60 |       16 |      225 |
| 2          |      4 |      20 |      −2 |     −10 |             20 |        4 |      100 |
| 3          |      6 |      30 |       0 |       0 |              0 |        0 |        0 |
| 4          |      8 |      35 |      +2 |      +5 |             10 |        4 |       25 |
| 5          |     10 |      50 |      +4 |     +20 |             80 |       16 |      400 |
| **Σ**      | **30** | **150** | **0 ✓** | **0 ✓** |        **170** |   **40** |  **750** |

**Schritt 4 · Einsetzen**

$$
r = \frac{170}{\sqrt{40 \cdot 750}} = \frac{170}{\sqrt{30\,000}} = \frac{170}{173{,}2} \approx \mathbf{0{,}98}
$$

**Schritt 5 · In Worte fassen**

> _„r = 0,98: ein starker gleichläufiger Zusammenhang. Je weiter der Kunde entfernt wohnt, desto länger dauert die Lieferung. Die Punkte liegen fast genau auf einer Geraden."_

Das ist auch **fachlich plausibel**: Weitere Strecken brauchen mehr Zeit. Wenn ein Ergebnis dem gesunden Menschenverstand und dem Fachwissen widerspricht, sollte man zuerst die Rechnung und die Daten prüfen.

### 🛡️ Drei Kontrollen gegen Rechenfehler

| #   | Kontrolle                                                               | Wenn sie fehlschlägt …                                        |
| --- | ----------------------------------------------------------------------- | ------------------------------------------------------------- |
| 1   | Die Spalten **x − x̄** und **y − ȳ** ergeben in der Summe jeweils **0**. | … ist ein Mittelwert falsch.                                  |
| 2   | r liegt **zwischen −1 und +1**.                                         | … fehlt meist ein Quadrat oder die Wurzel.                    |
| 3   | Das **Vorzeichen** passt zur Punktwolke.                                | … wurde ein Vorzeichen in einer Abweichungsspalte vertauscht. |

### ✏️ Aufgabe 3a · Heizkosten

Ein Haushalt notiert an fünf Wochen die **durchschnittliche Außentemperatur x (°C)** und die **Heizkosten y (€ pro Woche)**.

| Woche |   x |   y | x − x̄ | y − ȳ | (x − x̄)(y − ȳ) | (x − x̄)² | (y − ȳ)² |
| ----- | --: | --: | ----: | ----: | -------------: | -------: | -------: |
| 1     |   0 |  40 |       |       |                |          |          |
| 2     |   5 |  34 |       |       |                |          |          |
| 3     |  10 |  30 |       |       |                |          |          |
| 4     |  15 |  20 |       |       |                |          |          |
| 5     |  20 |  16 |       |       |                |          |          |
| **Σ** |     |     |       |       |                |          |          |

**a)** Berechne r. Denk an die drei Kontrollen.
**b)** Formuliere das Ergebnis in einem vollständigen Satz.

### ✏️ Aufgabe 3b · Schlaf und Tippfehler

Eine Person notiert an fünf Tagen, wie viele **Stunden sie geschlafen** hat (x) und wie viele **Tippfehler pro Seite** sie am nächsten Tag macht (y).

| Tag                |   1 |   2 |   3 |   4 |   5 |
| ------------------ | --: | --: | --: | --: | --: |
| x (Stunden Schlaf) |   5 |   6 |   7 |   8 |   9 |
| y (Tippfehler)     |   6 |   7 |   3 |   4 |   5 |

**a)** Berechne r mit der vollständigen Tabelle.
**b)** Formuliere das Ergebnis in einem Satz.
**c)** Warum ist dieses Ergebnis mit Vorsicht zu genießen? _(Tipp: Wie viele Tage wurden notiert?)_

### ✏️ Aufgabe 3c · Wartung und Störungen

> 📽️ Auf den Folien: **Übung 1**

Ein Betrieb vergleicht fünf Anlagen. x ist die **Anzahl der Wartungen pro Jahr**, y die **Anzahl der Störungen pro Jahr**.

| Anlage |   x |   y | x − x̄ | y − ȳ | (x − x̄)(y − ȳ) | (x − x̄)² | (y − ȳ)² |
| ------ | --: | --: | ----: | ----: | -------------: | -------: | -------: |
| B1     |   1 |   9 |       |       |                |          |          |
| B2     |   2 |   8 |       |       |                |          |          |
| B3     |   3 |   6 |       |       |                |          |          |
| B4     |   4 |   5 |       |       |                |          |          |
| B5     |   5 |   2 |       |       |                |          |          |
| **Σ**  |     |     |       |       |                |          |          |

**a)** Berechne r. Lege dazu die vollständige Tabelle an.
**b)** Formuliere das Ergebnis in einem Satz.
**c)** Darfst du daraus schließen, dass häufigere Wartung die Störungen senkt?

> 💡 Teil c) kannst du jetzt schon aus dem Bauch beantworten. Nach Kapitel 6 bis 8 schaust du dir deine Antwort noch einmal an.

### 🐍 Python-Aufgabe 3 · r selbst programmieren

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

## 4 · Grenze 1: r ist nicht die Steigung

### 📖 Erklärung

Ein häufiger Denkfehler: _„r ist hoch, also hat x eine große Wirkung auf y."_ Das stimmt nicht.

- **r** sagt, wie **eng** die Punkte an der Geraden liegen, also wie **verlässlich** der Zusammenhang ist.
- Die **Steigung** sagt, wie **stark** y reagiert, wenn x um 1 steigt, also wie **groß die Wirkung** ist.

Beides hat nichts miteinander zu tun. Eine Gerade kann flach und trotzdem eng sein, oder steil und trotzdem locker gestreut.

```
   r = 0,90 · flach                        r = 0,90 · steil
   y                                       y
   │                                       │                 •
   │                                       │            •
   │                                       │        •
   │  •  •  •  •  •                        │   •
   │                                       │•
   └──────────────── x                     └──────────────── x
```

> 📌 **Merksatz:** r sagt, **wie eng** der Zusammenhang ist. Die Steigung sagt, **wie groß die Wirkung** ist. Für eine Entscheidung brauchst du **beides**.

**Alltagsbeispiel:** Du stellst fest, dass dein Kaffeekonsum sehr eng mit deiner Konzentration zusammenhängt (r = 0,95). Pro Tasse steigt die Konzentration aber nur um 0,1 %. Der Zusammenhang ist verlässlich, aber praktisch bedeutungslos.

### 🧮 Rechenbeispiel · Zwei Maschinen

Zwei Maschinen laufen auf fünf Drehzahlstufen x. Gemessen wird die Temperaturerhöhung y (°C).

| Stufe x       |   1 |   2 |   3 |   4 |   5 |
| ------------- | --: | --: | --: | --: | --: |
| Maschine A: y |  10 |  12 |  11 |  13 |  14 |
| Maschine B: y |  10 |  30 |  20 |  40 |  50 |

**Maschine A:** x̄ = 3, ȳ = 12

| x − x̄    |  −2 |  −1 |   0 |  +1 |  +2 |  **Σ** |
| -------- | --: | --: | --: | --: | --: | -----: |
| y − ȳ    |  −2 |   0 |  −1 |  +1 |  +2 |    0 ✓ |
| Produkt  |   4 |   0 |   0 |   1 |   4 |  **9** |
| (x − x̄)² |   4 |   1 |   0 |   1 |   4 | **10** |
| (y − ȳ)² |   4 |   0 |   1 |   1 |   4 | **10** |

r = 9 / √(10 · 10) = 9 / 10 = **0,90**

**Maschine B:** x̄ = 3, ȳ = 30

| x − x̄    |  −2 |  −1 |   0 |  +1 |  +2 |    **Σ** |
| -------- | --: | --: | --: | --: | --: | -------: |
| y − ȳ    | −20 |   0 | −10 | +10 | +20 |      0 ✓ |
| Produkt  |  40 |   0 |   0 |  10 |  40 |   **90** |
| (x − x̄)² |   4 |   1 |   0 |   1 |   4 |   **10** |
| (y − ȳ)² | 400 |   0 | 100 | 100 | 400 | **1000** |

r = 90 / √(10 · 1000) = 90 / 100 = **0,90**

**Gleiches r, aber:** Die Steigung (bekannt von der Ausgleichsgeraden: Σ Produkte / Σ (x − x̄)²) ist bei A nur **0,9 °C pro Stufe**, bei B **9 °C pro Stufe**, also zehnmal so viel.

### ✏️ Aufgabe 4 · Welche Maßnahme lohnt sich?

Eine Firma untersucht zwei mögliche Stellschrauben für die Kundenzufriedenheit (Punkte von 0 bis 100):

| Maßnahme                                         | r mit Zufriedenheit | Steigung                              |
| ------------------------------------------------ | ------------------: | ------------------------------------- |
| A: Antwortzeit im Support verkürzen              |               −0,91 | −0,2 Punkte pro Stunde schneller      |
| B: Kostenloser Versand ab geringerem Bestellwert |               +0,55 | +8 Punkte pro 10 € niedrigerer Grenze |

**a)** Beschreibe beide Zusammenhänge in Worten.
**b)** Welche Maßnahme hat den **verlässlicheren** Zusammenhang, welche die **größere Wirkung**?
**c)** Warum reicht r allein nicht, um zu entscheiden?

### 🐍 Python-Aufgabe 4 · r und Steigung vergleichen

```python
import numpy as np

stufe = np.array([1, 2, 3, 4, 5])
temp_a = np.array([10, 12, 11, 13, 14])
temp_b = np.array([10, 30, 20, 40, 50])

for name, y in [("A", temp_a), ("B", temp_b)]:
    r = ...                                   # TODO
    steigung, achsenabschnitt = np.polyfit(stufe, y, 1)
    print(f"Maschine {name}: r = {r:.2f}, Steigung = {steigung:.1f} °C pro Stufe")
```

**a)** Ergänze r und führe das Skript aus.
**b)** Erzeuge eine Maschine C, bei der r **gleich** bleibt, die Steigung aber **negativ** ist. _(Tipp: Wie muss sich y verändern?)_ Oder geht das gar nicht? Begründe.
**c)** Zeichne alle Maschinen mit `plt.scatter` in ein gemeinsames Diagramm.

---

## 5 · Grenze 2: r = 0 heißt nicht „kein Zusammenhang"

### 📖 Erklärung

r misst nur eine Sache: **Wie gut passt eine gerade Linie?** Ist der Zusammenhang gebogen, kann r ihn übersehen, selbst wenn er perfekt ist.

Denk an die Raumtemperatur im Büro: Ist es zu kalt, kann man sich schlecht konzentrieren. Ist es zu warm, auch nicht. Irgendwo in der Mitte liegt das Optimum. Der Zusammenhang ist eindeutig da, aber er ist **bogenförmig**, nicht gerade.

Dazu kommt eine zweite Falle: **Ausreißer**. Ein einziger extremer Punkt kann r komplett verändern.

> 📌 **Merksatz:** r = 0 heißt nur: **kein linearer** Zusammenhang. Deshalb gilt immer: **Erst schauen, dann rechnen.**

### 🧮 Rechenbeispiel · Raumtemperatur und Konzentration

| x (Raumtemperatur °C)          |  16 |  18 |  20 |  22 |  24 |
| ------------------------------ | --: | --: | --: | --: | --: |
| y (Konzentrationstest, Punkte) |  60 |  80 |  90 |  80 |  60 |

```
  90 │           •
  80 │      •         •
  70 │
  60 │ •                   •
     └──┬────┬────┬────┬────┬──
       16   18   20   22   24     °C
```

x̄ = 20, ȳ = 74

| x − x̄   |      −4 |      −2 |     0 |      +2 |      +4 | **Σ** |
| ------- | ------: | ------: | ----: | ------: | ------: | ----: |
| y − ȳ   |     −14 |      +6 |   +16 |      +6 |     −14 |   0 ✓ |
| Produkt | **+56** | **−12** | **0** | **+12** | **−56** | **0** |

Der Zähler ist **0**, also ist **r = 0**. Die linke Hälfte (steigend) und die rechte Hälfte (fallend) heben sich genau auf. Dabei ist der Zusammenhang offensichtlich.

### 🧮 Rechenbeispiel · Ein Ausreißer

Fünf Punkte ohne erkennbaren Zusammenhang: (1|3), (2|5), (3|2), (4|4), (5|3) → **r ≈ −0,14**

Jetzt kommt **ein einziger** Punkt dazu: (12|12) → **r ≈ +0,88**

Ein Punkt macht aus „kein Zusammenhang" einen „starken Zusammenhang". Vielleicht ist es ein Messfehler, vielleicht ein echter Sonderfall. Das siehst du nur im Streudiagramm.

### ✏️ Aufgabe 5 · Erst schauen, dann rechnen

Ein Café notiert die **Anzahl Sonnenstunden x** und die **verkauften heißen Getränke y**:

| x   |   0 |   2 |   4 |   6 |   8 |
| --- | --: | --: | --: | --: | --: |
| y   |  50 |  80 |  90 |  80 |  50 |

**a)** Zeichne das Streudiagramm (Skizze reicht). Was vermutest du über r?
**b)** Berechne r.
**c)** Formuliere eine mögliche Erklärung für dieses Muster.
**d)** Was würdest du antworten, wenn jemand sagt: _„r ist null, die Sonne hat also keinen Einfluss auf den Verkauf"_?

### 🐍 Python-Aufgabe 5 · Bogen und Ausreißer

```python
import numpy as np
import matplotlib.pyplot as plt

# Teil 1: Bogen
rng = np.random.default_rng(1)
raumtemp = np.linspace(14, 28, 40)
konzentration = 90 - 1.2 * (raumtemp - 21) ** 2 + rng.normal(0, 3, 40)

# TODO a) r für alle Punkte berechnen und ausgeben
# TODO b) Daten bei 21 °C teilen und r für beide Hälften getrennt berechnen
# TODO c) Streudiagramm zeichnen

# Teil 2: Ausreißer
x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 2, 4, 3])
# TODO d) r berechnen, dann den Punkt (12|12) mit np.append hinzufügen und r erneut berechnen
```

**e)** Was lernst du aus Teil 1 b)? Wann ist es sinnvoll, Daten aufzuteilen?

---

## 6 · Vier Erklärungen für eine Korrelation

### 📖 Erklärung

Jetzt kommt der wichtigste Teil. Angenommen, du findest eine starke Korrelation zwischen x und y. Dann gibt es **vier mögliche Erklärungen**, und die Zahl r sagt dir **nie**, welche davon zutrifft.

```
  ① ZUFALL             ② UMGEKEHRTE RICHTUNG    ③ STÖRVARIABLE           ④ ECHTE KAUSALITÄT

    x       y            x ◀────────── y              z                    x ──────────▶ y
   (kein echter                                     ╱   ╲
    Zusammenhang)                                  ▼     ▼
                                                  x       y
```

| Erklärung                 | Was dahintersteckt                                                                                                                                                           | Beispiel                                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **① Zufall**              | Die Daten zeigen zufällig ein Muster, das es in Wirklichkeit nicht gibt. Je mehr Merkmale man durchsucht und je weniger Datenpunkte man hat, desto wahrscheinlicher ist das. | In den USA korrelierte über Jahre die Zahl der Filme mit Nicolas Cage mit der Zahl der Menschen, die in Pools ertrunken sind.                                     |
| **② Umgekehrte Richtung** | Nicht x verursacht y, sondern y verursacht x.                                                                                                                                | In Filialen mit mehr Überwachungskameras wird mehr gestohlen. Die Kameras locken keine Diebe an, sondern wo viel gestohlen wird, werden Kameras aufgehängt.       |
| **③ Störvariable**        | Eine dritte Größe z beeinflusst x **und** y gleichzeitig. Zwischen x und y selbst gibt es keine Verbindung.                                                                  | Bei Grundschulkindern korreliert die Schuhgröße mit der Lesefähigkeit. Die Störvariable ist das **Alter**: Ältere Kinder haben größere Füße **und** lesen besser. |
| **④ Echte Kausalität**    | x verursacht tatsächlich y.                                                                                                                                                  | Mehr gefahrene Kilometer verursachen mehr Reifenabrieb. Das wissen wir aus der Physik, nicht aus r.                                                               |

> ⚠️ **Die Störvariable ist der häufigste und gefährlichste Fall.** Die Korrelation ist echt, die Rechnung stimmt, nur der **Schluss** ist falsch. Und anders als beim Beispiel mit den Schuhen ist die dritte Größe im Betrieb oft unsichtbar.

### 🧮 Beispiel · Eine Störvariable im Betrieb

Ein Unternehmen stellt fest: **Laptops mit schwarzem Gehäuse** gehen seltener kaputt als silberne. Soll man nur noch schwarze Laptops kaufen?

```
   WAS MAN ZU SEHEN GLAUBT                  WAS TATSÄCHLICH VORLIEGT

      Gehäusefarbe                              Kaufjahr
           │                                  ╱          ╲
           │  (scheinbar)                    ▼            ▼
           ▼                           Gehäusefarbe    Defektrate
       Defektrate
                                       Schwarze Modelle gibt es erst seit zwei Jahren.
   Diesen Pfeil gibt es nicht.         Sie sind einfach jünger.
```

Das **Kaufjahr** ist die Störvariable. Neue Laptops sind schwarz **und** gehen seltener kaputt, weil sie neu sind. Die Farbe selbst bewirkt nichts.

### ✏️ Aufgabe 6a · Welche Erklärung passt?

Ordne jeder Beobachtung die wahrscheinlichste Erklärung zu (Zufall, umgekehrte Richtung, Störvariable, echte Kausalität). Begründe in einem Satz. Nenne, wenn möglich, eine zweite denkbare Erklärung.

| #   | Beobachtung                                                                                                                        |
| --- | ---------------------------------------------------------------------------------------------------------------------------------- |
| 1   | In Städten mit mehr Feuerwehrleuten gibt es mehr Brände.                                                                           |
| 2   | Mitarbeitende, die mehr Weiterbildungen besuchen, verdienen mehr.                                                                  |
| 3   | Menschen, die viel Schmerzmittel nehmen, haben häufiger Kopfschmerzen.                                                             |
| 4   | Ein Analyst testet 500 Kennzahlen gegen den Tagesumsatz. Die Anzahl der Buchstaben im Namen des Wochentags korreliert mit r = 0,6. |
| 5   | Server mit mehr Betriebsstunden haben häufiger Festplattendefekte.                                                                 |
| 6   | Hobbysportler mit mehr Trainingsstunden haben mehr Verletzungen.                                                                   |

> 💡 Bei manchen Beobachtungen sind zwei Antworten vertretbar. Wichtig ist die **Begründung**, nicht das Etikett.

### ✏️ Aufgabe 6b · Fälle aus dem Betrieb

> 📽️ Auf den Folien: **Übung 2** · Partnerarbeit

Zufall, umgekehrte Richtung, Störvariable oder echte Kausalität? Begründe und zieh, wo es passt, einen Vergleich zu einem Beispiel aus diesem Skript.

| #   | Beobachtung                                                                               |
| --- | ----------------------------------------------------------------------------------------- |
| 1   | Geräte, die im Sommer in Betrieb genommen wurden, fallen häufiger aus.                    |
| 2   | Anlagen mit höherem Stromverbrauch haben mehr Betriebsstunden.                            |
| 3   | Kunden, die den Support häufiger anrufen, kündigen seltener.                              |
| 4   | In Wochen mit vielen Krankmeldungen in der Werkstatt gibt es mehr ungeplante Stillstände. |
| 5   | Von 200 untersuchten Merkmalen korreliert die Nummer des Lagerregals mit der Ausfallrate. |

**Zusatz:** Schau dir jetzt noch einmal deine Antwort auf **Aufgabe 3c c)** an. Welche der vier Erklärungen kommen dort infrage?

### 🐍 Python-Aufgabe 6 · Zufallstreffer finden

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

## 7 · Vorhersagen oder entscheiden?

### 📖 Erklärung

Zurück zur Premium-Kreditkarte aus Kapitel 1. Kunden mit Premium-Karte bestellen mehr. Ist das nützlich? **Das hängt davon ab, was du vorhast.**

|                       | **Vorhersagen**                                                                      | **Entscheiden / eingreifen**                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Die Frage             | „Was wird passieren?"                                                                | „Was sollen wir tun?"                                                                                                      |
| Reicht Korrelation?   | **Ja.** Ein verlässliches Kennzeichen genügt.                                        | **Nein.** Es braucht Kausalität.                                                                                           |
| Kreditkarten-Beispiel | Ein Modell darf die Premium-Karte nutzen, um vorherzusagen, wer viel bestellen wird. | Allen eine Premium-Karte zu schenken, bringt nichts. Die Karte ist nur ein Hinweis auf hohes **Einkommen** (Störvariable). |
| Risiko                | **Drift:** Wenn sich der Zusammenhang ändert, wird das Modell unbemerkt schlechter.  | **Geld für eine Maßnahme, die nichts bewirkt.**                                                                            |

**Was ist Drift?** Angenommen, eine Bank verschenkt plötzlich Premium-Karten an alle Studierenden. Dann steht die Karte nicht mehr für hohes Einkommen, und das Modell, das auf die Karte gesetzt hat, liegt plötzlich daneben. Es merkt das aber nicht selbst. Deshalb ist es besser, wenn ein Modell die **echte Ursache** als Merkmal nutzt, sofern man sie kennt.

> 📌 **Merksatz:** Für eine **Vorhersage** genügt ein verlässlicher Zusammenhang. Für eine **Entscheidung** über eine Maßnahme brauchst du **Kausalität**.

### ✏️ Aufgabe 7 · Vorhersage oder Entscheidung?

Entscheide jeweils: Geht es um eine Vorhersage oder um eine Entscheidung? Reicht die Korrelation? Welches Risiko besteht?

1. Ein Modell sagt voraus, welche Laptops im nächsten Jahr kaputtgehen, und nutzt dafür die Gehäusefarbe.
2. Der Einkauf will ab sofort nur noch schwarze Laptops bestellen, weil die seltener kaputtgehen.
3. Eine Versicherung stellt fest, dass Kunden, die online abschließen, seltener Schäden melden. Sie möchte das in der Tarifberechnung nutzen.
4. Dieselbe Versicherung überlegt, allen Kunden einen Rabatt zu geben, wenn sie online abschließen, damit es weniger Schäden gibt.

---

## 8 · Wie man Kausalität prüft

### 📖 Erklärung

Wenn die Zahlen allein nichts über Ursache und Wirkung sagen, was dann? Es gibt vier Wege. Sie sind von **schnell und billig** bis **aufwendig und sicher** sortiert.

```
                                                         ┌──────────────────┐
                                                         │ ④ EXPERIMENT     │ ← einziger
                                           ┌─────────────┤                  │   echter Beweis
                                           │ ③ STÖR-     │                  │
                             ┌─────────────┤ VARIABLE    │                  │
                             │ ② ZEIT-     │ KONTROL-    │                  │
               ┌─────────────┤ LICHE REI-  │ LIEREN      │                  │
               │ ① FACH-     │ HENFOLGE    │             │                  │
               │ WISSEN      │             │             │                  │
  ─────────────┴─────────────┴─────────────┴─────────────┴──────────────────┴────▶
   schnell, billig                                              aufwendig, sicher
```

| Weg                              | Leitfrage                                                                 | Am Laptop-Beispiel                                                                                                          |
| -------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| **① Fachwissen**                 | Gibt es einen plausiblen Mechanismus?                                     | IT fragen: Kann die Farbe des Gehäuses Defekte beeinflussen? Vermutlich nicht.                                              |
| **② Zeitliche Reihenfolge**      | Kommt die Ursache vor der Wirkung?                                        | Die Ursache muss zeitlich vorher da sein. Das schließt die umgekehrte Richtung aus, beweist aber noch keine Kausalität.     |
| **③ Störvariable kontrollieren** | Bleibt der Zusammenhang, wenn man nur **vergleichbare** Fälle vergleicht? | Nur Laptops **gleichen Alters** vergleichen. Ist die Defektrate dann bei beiden Farben gleich, war das Alter die Erklärung. |
| **④ Experiment**                 | Was passiert, wenn man gezielt eingreift?                                 | Zwei **zufällig** gebildete Gruppen, nur eine bekommt die Veränderung.                                                      |

**Warum „zufällig" beim Experiment so wichtig ist:** Wenn man die Gruppen per Zufall bildet, verteilen sich **alle** möglichen Störvariablen gleichmäßig auf beide Gruppen, auch die, an die niemand gedacht hat. Ein Unterschied am Ende kann dann nur noch von der Veränderung kommen.

> 📌 **Im Alltag am nützlichsten ist Weg ③:** Er braucht nur die Daten, die schon da sind, und oft nur eine halbe Stunde Arbeit.

### ✏️ Aufgabe 8 · Einen Prüfplan schreiben

Wähle **eine** Beobachtung aus Aufgabe 6a oder 6b (z. B. Weiterbildungen und Gehalt). Beschreibe für jeden der vier Wege in ein bis zwei Sätzen, wie du konkret vorgehen würdest. Welchen Weg gehst du **zuerst**, und warum?

### 🐍 Python-Aufgabe 8 · Eine Störvariable entlarven

Wir simulieren zehn Jahre Freibad-Daten. **Eisverkauf** und **Sonnenbrände** hängen beide **nur** von der Temperatur ab, nicht voneinander.

```python
import numpy as np
import pandas as pd

rng = np.random.default_rng(7)
n = 3650
temperatur = rng.uniform(0, 35, n)                           # die Störvariable
eis = 20 + 8 * temperatur + rng.normal(0, 30, n)             # hängt NUR von der Temperatur ab
sonnenbrand = 1 + 0.4 * temperatur + rng.normal(0, 2, n)     # hängt NUR von der Temperatur ab

df = pd.DataFrame({"temperatur": temperatur, "eis": eis, "sonnenbrand": sonnenbrand})

# TODO a) Korrelationsmatrix mit df.corr() ausgeben. Wie stark korrelieren eis und sonnenbrand?

# TODO b) Weg 3: Temperaturklassen à 1 °C bilden
df["temp_klasse"] = pd.cut(df["temperatur"], bins=range(0, 36, 1))

# TODO c) Für jede Klasse r(eis, sonnenbrand) berechnen und den Durchschnitt ausgeben
#         Tipp: for klasse, gruppe in df.groupby("temp_klasse", observed=True): ...
```

**d)** Vergleiche das r aus a) mit dem Durchschnitt aus c). Was beweist das?
**e)** Übertrage das Vorgehen auf das Laptop-Beispiel: Welche Spalten bräuchtest du, und wie würdest du gruppieren?

---

## 9 · Das Wichtigste auf einen Blick

|                       |                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------- |
| **r misst**           | Richtung (Vorzeichen) und Stärke (Betrag) eines **linearen** Zusammenhangs, immer zwischen −1 und +1. |
| **Drei Kontrollen**   | Abweichungen summieren sich zu 0 · r liegt zwischen −1 und +1 · Vorzeichen passt zur Punktwolke.      |
| **r misst nicht**     | die Steigung. Ein enger Zusammenhang kann eine winzige Wirkung haben.                                 |
| **r = 0 heißt**       | nur: kein **linearer** Zusammenhang. Bögen und Ausreißer sieht man nur im Diagramm.                   |
| **Vier Erklärungen**  | Zufall · umgekehrte Richtung · Störvariable · echte Kausalität. r sagt nie, welche.                   |
| **Störvariable**      | der häufigste und gefährlichste Fall: Die Rechnung stimmt, nur der Schluss ist falsch.                |
| **Vorhersage**        | darf jedes verlässliche Merkmal nutzen, auch ohne Kausalität (Risiko: Drift).                         |
| **Entscheidung**      | braucht Kausalität, sonst zahlt man für eine Maßnahme ohne Wirkung.                                   |
| **Kausalität prüfen** | Fachwissen · zeitliche Reihenfolge · Störvariable kontrollieren · Experiment.                         |

> 🔁 **Erst schauen, dann rechnen. Korrelation ist nicht Kausalität.**

### 🎯 Für die Prüfung

- r kommt als **Rechenaufgabe mit 4 bis 6 Wertepaaren** in genau dieser Tabellenform.
- Die Zahl allein ist nur die halbe Antwort. **Punkte gibt es auch für den Satz in Worten.**
- Die häufigste Falle: aus einer starken Korrelation auf eine Ursache schließen.
- Für das Fachgespräch: Überleg dir ein **eigenes Beispiel für eine Störvariable aus deinem Betrieb**.

---

---

# Lösungen

## Lösung Aufgabe 2 · r in Worte fassen

1. **r = −0,82:** starker gegenläufiger Zusammenhang. Wer mehr trainiert, läuft die 10 km tendenziell schneller (kürzere Zeit).
2. **r = −0,45:** mittlerer gegenläufiger Zusammenhang. Mit mehr Personal wird die Wartezeit tendenziell kürzer, aber die Werte streuen deutlich.
3. **r = +0,63:** mittlerer gleichläufiger Zusammenhang. Mehr Werbebudget geht tendenziell mit mehr Umsatz einher.
4. **r = +0,02:** kein linearer Zusammenhang. Zusätzlich ist die Frage fachlich sinnlos: Hausnummern sind nur Namen, keine Messwerte. Mit ihnen zu rechnen, ergibt keinen Sinn.

## Lösung Python-Aufgabe 2

```python
y = r * x + np.sqrt(1 - r**2) * rauschen
gemessen = np.corrcoef(x, y)[0, 1]
```

**c)** Die Daten sind zufällig, deshalb trifft die Stichprobe das Ziel nie ganz genau. Mit nur 10 Punkten schwankt das gemessene r viel stärker. Bei kleinen Datensätzen ist r unsicher.

## Lösung Aufgabe 3a · Heizkosten

x̄ = 50 / 5 = **10**, ȳ = 140 / 5 = **28**

| Woche |      x |       y |   x − x̄ |   y − ȳ | (x − x̄)(y − ȳ) | (x − x̄)² | (y − ȳ)² |
| ----- | -----: | ------: | ------: | ------: | -------------: | -------: | -------: |
| 1     |      0 |      40 |     −10 |     +12 |           −120 |      100 |      144 |
| 2     |      5 |      34 |      −5 |      +6 |            −30 |       25 |       36 |
| 3     |     10 |      30 |       0 |      +2 |              0 |        0 |        4 |
| 4     |     15 |      20 |      +5 |      −8 |            −40 |       25 |       64 |
| 5     |     20 |      16 |     +10 |     −12 |           −120 |      100 |      144 |
| **Σ** | **50** | **140** | **0 ✓** | **0 ✓** |       **−310** |  **250** |  **392** |

$$
r = \frac{-310}{\sqrt{250 \cdot 392}} = \frac{-310}{\sqrt{98\,000}} = \frac{-310}{313{,}0} \approx \mathbf{-0{,}99}
$$

**b)** _„r = −0,99: ein sehr starker gegenläufiger Zusammenhang. Je wärmer es draußen ist, desto niedriger sind die Heizkosten. Die Punkte liegen fast perfekt auf einer fallenden Geraden."_

## Lösung Aufgabe 3b · Schlaf und Tippfehler

x̄ = 35 / 5 = **7**, ȳ = 25 / 5 = **5**

| Tag   |      x |      y |   x − x̄ |   y − ȳ | (x − x̄)(y − ȳ) | (x − x̄)² | (y − ȳ)² |
| ----- | -----: | -----: | ------: | ------: | -------------: | -------: | -------: |
| 1     |      5 |      6 |      −2 |      +1 |             −2 |        4 |        1 |
| 2     |      6 |      7 |      −1 |      +2 |             −2 |        1 |        4 |
| 3     |      7 |      3 |       0 |      −2 |              0 |        0 |        4 |
| 4     |      8 |      4 |      +1 |      −1 |             −1 |        1 |        1 |
| 5     |      9 |      5 |      +2 |       0 |              0 |        4 |        0 |
| **Σ** | **35** | **25** | **0 ✓** | **0 ✓** |         **−5** |   **10** |   **10** |

$$
r = \frac{-5}{\sqrt{10 \cdot 10}} = \frac{-5}{10} = \mathbf{-0{,}5}
$$

**b)** _„r = −0,5: ein mittlerer gegenläufiger Zusammenhang. Nach mehr Schlaf macht die Person tendenziell weniger Tippfehler, die Werte streuen aber deutlich."_

**c)** Fünf Tage sind sehr wenig. Bei so wenigen Werten kann ein mittleres r auch rein zufällig entstehen. Ein einzelner ungewöhnlicher Tag verändert das Ergebnis stark. Außerdem sind Störvariablen denkbar, etwa Stress oder Kaffee.

## Lösung Aufgabe 3c · Wartung und Störungen

x̄ = 15 / 5 = **3**, ȳ = 30 / 5 = **6**

| Anlage |      x |      y |   x − x̄ |   y − ȳ | (x − x̄)(y − ȳ) | (x − x̄)² | (y − ȳ)² |
| ------ | -----: | -----: | ------: | ------: | -------------: | -------: | -------: |
| B1     |      1 |      9 |      −2 |      +3 |             −6 |        4 |        9 |
| B2     |      2 |      8 |      −1 |      +2 |             −2 |        1 |        4 |
| B3     |      3 |      6 |       0 |       0 |              0 |        0 |        0 |
| B4     |      4 |      5 |      +1 |      −1 |             −1 |        1 |        1 |
| B5     |      5 |      2 |      +2 |      −4 |             −8 |        4 |       16 |
| **Σ**  | **15** | **30** | **0 ✓** | **0 ✓** |        **−17** |   **10** |   **30** |

$$
r = \frac{-17}{\sqrt{10 \cdot 30}} = \frac{-17}{\sqrt{300}} = \frac{-17}{17{,}32} \approx \mathbf{-0{,}98}
$$

**b)** _„r = −0,98: ein sehr starker gegenläufiger Zusammenhang. Anlagen, die häufiger gewartet werden, haben weniger Störungen. Die Punkte liegen fast genau auf einer fallenden Geraden."_

**c)** **Nein, nicht allein aus dieser Rechnung.** Ein hohes r sagt nichts darüber, _warum_ die beiden Größen zusammenhängen (Kapitel 6). Alle vier Erklärungen kommen infrage:

- **Störvariable:** Wie bei den schwarzen Laptops das **Kaufjahr** könnte hier das **Alter der Anlagen** dahinterstecken. Neuere Anlagen werden vielleicht häufiger gewartet, etwa wegen eines Wartungsvertrags, und haben ohnehin weniger Störungen.
- **Umgekehrte Richtung:** Wie bei den Überwachungskameras kann die Wirkung andersherum laufen. Anlagen mit vielen Störungen stehen so oft still oder in Reparatur, dass die planmäßige Wartung ausfällt.
- **Zufall:** Fünf Anlagen sind sehr wenig, genau wie die fünf Tage in Aufgabe 3b.
- **Echte Kausalität** ist fachlich plausibel: Wartung soll ja Störungen verhindern. Das ist aber Fachwissen (Weg ①), kein Beweis.

Wer das Wartungsintervall ändern will, trifft eine **Entscheidung** und braucht deshalb Kausalität (Kapitel 7). Prüfen könnte man das mit Weg ③ (nur Anlagen **gleichen Alters** vergleichen, wie beim Laptop-Beispiel) oder mit Weg ④ (Wartungsintervall bei **zufällig** ausgewählten Anlagen ändern).

## Lösung Python-Aufgabe 3

```python
def korrelation(x, y):
    dx = x - x.mean()
    dy = y - y.mean()
    zaehler = np.sum(dx * dy)
    nenner = np.sqrt(np.sum(dx**2) * np.sum(dy**2))
    return zaehler / nenner
```

**b)** Heizkosten: −0,990 · Schlaf: −0,500 · Wartung: −0,981
**c)** Beide Summen sind 0 (bzw. `0.0`). Das ist Kontrolle 1: Die Abweichungen vom Mittelwert heben sich immer auf.

## Lösung Aufgabe 4 · Welche Maßnahme lohnt sich?

**a)** A: starker gegenläufiger Zusammenhang. Je kürzer die Antwortzeit, desto zufriedener die Kunden (negatives r, weil weniger Stunden mit mehr Zufriedenheit einhergehen). B: mittlerer gleichläufiger Zusammenhang zwischen niedrigerer Versandgrenze und Zufriedenheit.
**b)** **A ist verlässlicher** (|r| = 0,91), **B hat die größere Wirkung** (8 Punkte pro 10 € gegenüber 0,2 Punkten pro Stunde).
**c)** r sagt nur, wie eng der Zusammenhang ist. Ob sich eine Maßnahme lohnt, hängt von der **Wirkung** (Steigung) und den **Kosten** ab. Außerdem müsste man vor einer Entscheidung klären, ob der Zusammenhang überhaupt **kausal** ist (Kapitel 6 bis 8).

## Lösung Python-Aufgabe 4

```python
r = np.corrcoef(stufe, y)[0, 1]
```

Ausgabe:

```
Maschine A: r = 0.90, Steigung = 0.9 °C pro Stufe
Maschine B: r = 0.90, Steigung = 9.0 °C pro Stufe
```

**b)** Das geht nicht. Wenn die Steigung negativ wird, fällt die Punktwolke, und dann wird auch r negativ. **Das Vorzeichen von r und das Vorzeichen der Steigung sind immer gleich.** Nur der **Betrag** kann unabhängig voneinander variieren. Mit z. B. `temp_c = 60 - temp_b` erhältst du r = −0,90 und eine Steigung von −9.

## Lösung Aufgabe 5 · Sonnenstunden und heiße Getränke

**a)** Die Punkte bilden einen umgekehrten Bogen. Vermutung: r ist nahe 0.

**b)** x̄ = 20 / 5 = **4**, ȳ = 350 / 5 = **70**

| Tag   |      x |       y |   x − x̄ |   y − ȳ | (x − x̄)(y − ȳ) | (x − x̄)² | (y − ȳ)² |
| ----- | -----: | ------: | ------: | ------: | -------------: | -------: | -------: |
| 1     |      0 |      50 |      −4 |     −20 |            +80 |       16 |      400 |
| 2     |      2 |      80 |      −2 |     +10 |            −20 |        4 |      100 |
| 3     |      4 |      90 |       0 |     +20 |              0 |        0 |      400 |
| 4     |      6 |      80 |      +2 |     +10 |            +20 |        4 |      100 |
| 5     |      8 |      50 |      +4 |     −20 |            −80 |       16 |      400 |
| **Σ** | **20** | **350** | **0 ✓** | **0 ✓** |          **0** |   **40** | **1400** |

$$
r = \frac{0}{\sqrt{40 \cdot 1400}} = \frac{0}{\sqrt{56\,000}} = \frac{0}{236{,}6} = \mathbf{0}
$$

Die positiven Produkte (links unten, rechts oben) und die negativen (links oben, rechts unten) heben sich **genau auf**. Der Zähler ist 0, also **r = 0**, obwohl die Punkte ein klares Muster bilden.

**c)** Bei null Sonnenstunden (Regen) gehen wenige Leute raus. Bei etwas Sonne kommen mehr Gäste und trinken Kaffee. Bei sehr viel Sonne ist es zu heiß für heiße Getränke, die Gäste bestellen lieber Kaltes.
**d)** r misst nur, ob eine **Gerade** passt. Hier gibt es einen deutlichen, aber **bogenförmigen** Zusammenhang. r = 0 heißt nur „kein linearer Zusammenhang", nicht „kein Einfluss".

## Lösung Python-Aufgabe 5

```python
# a)
r_gesamt = np.corrcoef(raumtemp, konzentration)[0, 1]
print(f"r gesamt: {r_gesamt:.2f}")                      # ca. -0.01

# b)
kalt = raumtemp <= 21
warm = raumtemp > 21
print(f"r bis 21 °C:  {np.corrcoef(raumtemp[kalt], konzentration[kalt])[0, 1]:.2f}")   # ca. +0.96
print(f"r über 21 °C: {np.corrcoef(raumtemp[warm], konzentration[warm])[0, 1]:.2f}")   # ca. -0.95

# c)
plt.scatter(raumtemp, konzentration)
plt.xlabel("Raumtemperatur (°C)")
plt.ylabel("Konzentration (Punkte)")
plt.show()

# d)
print(f"ohne Ausreißer: {np.corrcoef(x, y)[0, 1]:.2f}")                                # -0.14
x_neu, y_neu = np.append(x, 12), np.append(y, 12)
print(f"mit Ausreißer:  {np.corrcoef(x_neu, y_neu)[0, 1]:.2f}")                        # +0.88
```

**e)** Insgesamt ist r ≈ 0, aber in jeder Hälfte gibt es einen sehr starken Zusammenhang (+0,96 und −0,95). Aufteilen lohnt sich, wenn das Streudiagramm einen **Knick** oder **Wendepunkt** zeigt und es dafür einen fachlichen Grund gibt, hier die Wohlfühltemperatur.

## Lösung Aufgabe 6a · Welche Erklärung passt?

| #   | Beobachtung                             | Wahrscheinlichste Erklärung          | Begründung                                                                                                                      | Zweite denkbare Erklärung                                                                                                                                   |
| --- | --------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Mehr Feuerwehrleute ↔ mehr Brände       | **Störvariable**                     | Die **Größe der Stadt**: Große Städte haben mehr Einwohner, mehr Gebäude, mehr Brände **und** mehr Feuerwehr.                   | **Umgekehrte Richtung:** Wo es oft brennt, stellt man mehr Feuerwehrleute ein.                                                                              |
| 2   | Mehr Weiterbildungen ↔ mehr Gehalt      | **Störvariable** oder **Kausalität** | Motivation oder Position: Wer ohnehin ehrgeizig ist oder eine Führungsrolle hat, bildet sich mehr weiter **und** verdient mehr. | Echte Kausalität ist plausibel. **Umgekehrt** geht auch: Wer mehr verdient, bekommt eher Weiterbildungen bezahlt.                                           |
| 3   | Viel Schmerzmittel ↔ mehr Kopfschmerzen | **Umgekehrte Richtung**              | Wer häufig Kopfschmerzen hat, nimmt mehr Schmerzmittel.                                                                         | Auch **echte Kausalität** ist bekannt: Übermäßiger Gebrauch kann selbst Kopfschmerzen auslösen. Beides kann gleichzeitig stimmen.                           |
| 4   | Buchstaben im Wochentag ↔ Umsatz        | **Zufall**                           | Bei 500 getesteten Kennzahlen findet sich fast sicher eine mit hohem r. Einen fachlichen Grund gibt es nicht.                   | Denkbar ist höchstens eine Störvariable: Der Wochentag selbst beeinflusst den Umsatz (z. B. Samstag), und die Buchstabenzahl hängt zufällig damit zusammen. |
| 5   | Betriebsstunden ↔ Festplattendefekte    | **Echte Kausalität**                 | Mechanische Bauteile verschleißen mit der Laufzeit. Das stützt das Fachwissen.                                                  | Störvariable möglich: Ältere Server haben mehr Stunden **und** ältere Festplattenmodelle.                                                                   |
| 6   | Mehr Training ↔ mehr Verletzungen       | **Echte Kausalität**                 | Mehr Belastung führt zu mehr Gelegenheiten für Verletzungen.                                                                    | **Störvariable:** Wer viel trainiert, macht oft riskantere Sportarten oder Wettkämpfe.                                                                      |

## Lösung Aufgabe 6b · Fälle aus dem Betrieb

| #   | Beobachtung                                        | Wahrscheinlichste Erklärung                   | Begründung                                                                                                                                                                                                                               | Bezug im Skript                                                                                                                                                                              |
| --- | -------------------------------------------------- | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Sommer-Inbetriebnahme ↔ häufigere Ausfälle         | **Störvariable**                              | Die Jahreszeit selbst macht ein Gerät kaum anfälliger. Wahrscheinlicher ist, dass die Sommergeräte aus einer bestimmten **Lieferung oder Bauserie** stammen. Nachfragen statt raten.                                                     | Wie die **schwarzen Laptops**: Nicht die Farbe, sondern das Kaufjahr steckt dahinter. Prüfen mit Weg ③: nur Geräte derselben Serie vergleichen.                                              |
| 2   | Höherer Stromverbrauch ↔ mehr Betriebsstunden      | **Umgekehrte Richtung**                       | Nicht der Stromverbrauch erzeugt Betriebsstunden, sondern wer länger läuft, verbraucht mehr Strom. Der Zusammenhang ist trivial und bringt keine neue Erkenntnis.                                                                        | Wie die **Überwachungskameras**: Die vermutete Wirkung ist in Wahrheit die Ursache.                                                                                                          |
| 3   | Häufiger Support-Anrufe ↔ seltener Kündigung       | **Störvariable** oder **umgekehrte Richtung** | Engagierte Kunden rufen öfter an **und** bleiben eher. Die Kundenbindung verursacht beides.                                                                                                                                              | Wie die **Premium-Kreditkarte** (Kapitel 7): Für die **Vorhersage** von Kündigungen trotzdem nützlich. Kunden zum Anrufen zu drängen (**Entscheidung**) senkt die Kündigungen aber nicht.    |
| 4   | Viele Krankmeldungen ↔ mehr ungeplante Stillstände | **Störvariable**                              | In Zeiten hoher Belastung steigen beide. Auch **echte Kausalität** ist möglich: Weniger Personal bedeutet weniger vorbeugende Wartung. Sogar die **umgekehrte Richtung** ist denkbar: Viele Stillstände bedeuten Stress und Überstunden. | Hier hilft Weg ② (**zeitliche Reihenfolge**): Kommen die Krankmeldungen vor den Stillständen oder danach?                                                                                    |
| 5   | Regalnummer ↔ Ausfallrate (1 von 200 Merkmalen)    | **Zufall**                                    | Wer 200 Merkmale durchsucht, findet rein zufällig immer irgendeinen Zusammenhang. Außerdem ist eine Regalnummer nur ein Name und kein Messwert.                                                                                          | Genau das Experiment aus **Python-Aufgabe 6** und Aufgabe 6a Nr. 4 (Buchstaben im Wochentag). Die Regalnummer ist wie die **Hausnummer** in Aufgabe 2: damit zu rechnen, ergibt keinen Sinn. |

**Zusatz (Aufgabe 3c c):** Bei Wartung und Störungen kommen **alle vier** Erklärungen infrage. Siehe die [Lösung zu Aufgabe 3c](#lösung-aufgabe-3c--wartung-und-störungen).

## Lösung Python-Aufgabe 6

```python
r_werte = np.array([np.corrcoef(merkmale[:, i], ziel)[0, 1] for i in range(n_merkmale)])

bestes = np.argmax(np.abs(r_werte))
print(f"Bestes Merkmal: Nr. {bestes} mit r = {r_werte[bestes]:+.2f}")       # ca. -0.65
print(f"Merkmale mit |r| > 0,4: {np.sum(np.abs(r_werte) > 0.4)}")           # ca. 14

ziel_neu = rng.normal(size=n_tage)
merkmal_neu = rng.normal(size=n_tage)
print(f"Mit neuen Daten: r = {np.corrcoef(merkmal_neu, ziel_neu)[0, 1]:+.2f}")   # irgendwo um 0
```

**e)** Mit 200 Tagen werden die Zufalls-r deutlich kleiner. Je mehr Datenpunkte, desto seltener entsteht rein zufällig ein großes r.
**f)** **Erst die Vermutung, dann die Suche.** Wer ohne Hypothese Hunderte Merkmale durchsucht, findet immer etwas. Einen Fund sollte man deshalb mit **neuen Daten** bestätigen, bevor man ihm glaubt.

## Lösung Aufgabe 7 · Vorhersage oder Entscheidung?

1. **Vorhersage** → Korrelation reicht, die Farbe ist ein verlässliches Kennzeichen für das Alter. Risiko: **Drift**, sobald neue Modelle wieder silbern sind. Besser gleich das Kaufjahr als Merkmal verwenden.
2. **Entscheidung** → Kausalität nötig. Die Farbe verursacht keine Defekte, schwarze Laptops zu kaufen bringt nichts. Risiko: Geld ohne Wirkung.
3. **Vorhersage** → Für die Tarifberechnung reicht der Zusammenhang, solange er stabil bleibt. Risiko: Drift, wenn sich das Kundenverhalten ändert. _(Zusatz: Bei Entscheidungen über Menschen sind zusätzlich rechtliche Grenzen wie Diskriminierungsverbote zu beachten.)_
4. **Entscheidung** → Kausalität nötig. Vermutlich ist die Online-Abschlussart nur ein Hinweis auf eine Störvariable (z. B. jüngere, technikaffine Kunden mit anderem Risikoprofil). Ein Rabatt würde die Schäden dann nicht senken.

## Lösung Aufgabe 8 · Prüfplan (Beispiel: Weiterbildungen und Gehalt)

1. **Fachwissen:** Personalabteilung fragen, ob Weiterbildungen bei Gehaltsentscheidungen tatsächlich berücksichtigt werden.
2. **Zeitliche Reihenfolge:** Prüfen, ob das Gehalt **nach** einer Weiterbildung steigt oder ob Weiterbildungen erst **nach** einer Gehaltserhöhung bzw. Beförderung kommen.
3. **Störvariable kontrollieren:** Nur Mitarbeitende mit **gleicher Position, Betriebszugehörigkeit und Ausbildung** vergleichen. Bleibt der Unterschied bestehen?
4. **Experiment:** Weiterbildungsplätze unter interessierten Mitarbeitenden **per Los** vergeben und nach zwei Jahren die Gehaltsentwicklung beider Gruppen vergleichen.

**Zuerst** Weg ① und ③, weil sie schnell gehen und nur vorhandene Informationen brauchen. Das Experiment lohnt sich, wenn eine größere Investition davon abhängt.

## Lösung Python-Aufgabe 8

```python
# a)
print(df[["temperatur", "eis", "sonnenbrand"]].corr().round(2))
# eis ↔ sonnenbrand: ca. 0.84

# c)
werte = []
for klasse, gruppe in df.groupby("temp_klasse", observed=True):
    werte.append(gruppe["eis"].corr(gruppe["sonnenbrand"]))
print(f"r bei gleicher Temperatur (Durchschnitt): {np.mean(werte):+.2f}")   # ca. 0.00
```

**d)** Insgesamt korrelieren Eis und Sonnenbrand stark (r ≈ 0,84). Vergleicht man nur Tage mit **gleicher Temperatur**, verschwindet der Zusammenhang (r ≈ 0). Das zeigt: Die Temperatur ist die Störvariable, Eis und Sonnenbrand haben direkt nichts miteinander zu tun.
**e)** Man bräuchte die Spalten `farbe`, `kaufjahr` (bzw. Alter) und `defekt`. Dann nach Kaufjahr gruppieren und in jeder Gruppe die Defektrate von schwarzen und silbernen Laptops vergleichen: `df.groupby(["kaufjahr", "farbe"])["defekt"].mean()`.
