# Logische Puzzels: Lijsten
Datum: 1 mrt 2026
Onderwerp: Lijsten — Opbouwen, Filteren & Zoeken

*Vijf puzzels om de lijst te leren kennen — Python's meest gebruikte container. Een lijst bewaard meerdere waarden in één variabele: `mand = []` start leeg; `mand.append(x)` voegt `x` toe aan het einde; `len(mand)` vertelt hoeveel items erin zitten.*

---

## Puzzel 1: De Robot Fruitplucker (Makkelijk)
**Het Verhaal**: Een robot loopt langs bomen genummerd 1 tot en met 10. Hij plukt alleen fruit van een boom als het boomgetal **deelbaar is door 3**. Elk geplukt boomgetal wordt aan zijn mandlijst toegevoegd.

**De Vraag**: Bouw de `mand`-lijst met een lus. Wat zit er in de mand? Hoeveel fruit heeft hij geplukt, en wat is het totaalgewicht (boomgetal = gewicht in gram)?

**Voorbeeld Test**:
- Bomen 1 tot 6: bomen 3 en 6 zijn deelbaar door 3 → mand = `[3, 6]`, aantal = 2, totaal = 9.

**Hint**: Begin met `mand = []`. Gebruik in een lus van 1 tot 10: `if boom % 3 == 0:` en dan `mand.append(boom)`.

**Controleer je Logica**:
- Bomen 1–6: mand = `[3, 6]`, aantal = **2**, totaal = **9**.
- Bomen 1–10: mand = `[3, 6, 9]`, aantal = **3**, totaal = **18**.

```python
# Start Code
mand = []

for boom in range(1, 11):
    # Als het boomnummer deelbaar is door 3, voeg het toe aan mand
    pass

print(f"Mand: {mand}")
print(f"Aantal fruit: {len(mand)}")
print(f"Totaalgewicht: {sum(mand)} gram")
```

---

## Puzzel 2: Het Schoolrapport (Makkelijk–Gemiddeld)
**Het Verhaal**: Een leraar heeft 12 leerlingscores en wil twee aparte lijsten: één voor leerlingen die **geslaagd** zijn (score ≥ 60) en één voor leerlingen die **gezakt** zijn (score < 60).

**De Vraag**: Loop over de scores en vul de twee lijsten. Hoeveel zijn er geslaagd en hoeveel gezakt?

Scores: `[45, 72, 88, 55, 91, 60, 78, 43, 95, 67, 82, 50]`

**Voorbeeld Test**:
- Scores `[80, 55, 65]`: geslaagd = `[80, 65]`, gezakt = `[55]`.

**Hint**: Begin met `geslaagd = []` en `gezakt = []`. Gebruik `for score in scores:` en controleer daarbinnen `if score >= 60:` om te bepalen aan welke lijst je toevoegt.

**Controleer je Logica**:
- Geslaagd (score ≥ 60): 72, 88, 91, 60, 78, 95, 67, 82 → **8 leerlingen**.
- Gezakt (score < 60): 45, 55, 43, 50 → **4 leerlingen**.

```python
# Start Code
scores = [45, 72, 88, 55, 91, 60, 78, 43, 95, 67, 82, 50]
geslaagd = []
gezakt = []

for score in scores:
    # Voeg toe aan geslaagd of gezakt op basis van de score
    pass

print(f"Geslaagd: {geslaagd}")
print(f"Gezakt: {gezakt}")
print(f"Aantal geslaagd: {len(geslaagd)}, Aantal gezakt: {len(gezakt)}")
```

---

## Puzzel 3: Het Lopende Totaal van de Bakker (Gemiddeld)
**Het Verhaal**: Een bakker noteert zijn verdiensten elke dag van de week. Hij wil een "lopend totaal"-lijst — na elke dag, hoeveel heeft hij *tot nu toe* verdiend?

Dagelijkse verdiensten: `[12, 8, 15, 5, 20, 10, 18]`

**De Vraag**: Bouw een `lopende_totalen`-lijst waarbij elk item het cumulatieve totaal tot en met die dag is.

**Voorbeeld Test**:
- Dagelijks `[10, 5, 3]` → lopende totalen = `[10, 15, 18]`.

**Hint**: Houd een `totaal = 0`-variabele bij. Voeg voor elke `verdienste` in de lijst die toe aan `totaal`, en dan `lopende_totalen.append(totaal)`.

**Controleer je Logica**:
- Na dag 1: **12**.
- Na dag 3: **35** (12 + 8 + 15).
- Na dag 7 (eindtotaal): **88**.

```python
# Start Code
dagelijkse_verdiensten = [12, 8, 15, 5, 20, 10, 18]
lopende_totalen = []
totaal = 0

for verdienste in dagelijkse_verdiensten:
    # 1. Tel verdienste op bij totaal
    # 2. Voeg totaal toe aan lopende_totalen
    pass

print(f"Lopende totalen: {lopende_totalen}")
print(f"Eindtotaal: {totaal}")
```

---

## Puzzel 4: De Bergwandelaar (Gemiddeld–Moeilijk)
**Het Verhaal**: Een wandelaar noteert zijn **hoogteverandering** elk uur. Startend op 0 meter betekenen positieve getallen omhoog gaan en negatieve getallen omlaag gaan.

Uurlijkse veranderingen: `[3, -1, 5, -2, 4, -3, 6, -1, 2, -4]`

**De Vraag**: Bouw een `hoogtes`-lijst (hoogte na elk uur). Zoek daarna de **hoogste bereikte hoogte** — maar **zonder Python's ingebouwde `max()`-functie**. Gebruik een tweede lus om zelf door de lijst te zoeken.

**Voorbeeld Test**:
- Veranderingen `[3, -1, 5]` → hoogtes = `[3, 2, 7]`, hoogste = **7**.

**Hint**: Deel 1: start met `hoogte = 0`, loop over veranderingen, werk `hoogte` bij, voeg toe aan lijst. Deel 2: start `hoogste = 0`, loop over `hoogtes`, werk `hoogste` bij als de huidige waarde groter is.

**Controleer je Logica**:
- Hoogtes-lijst: `[3, 2, 7, 5, 9, 6, 12, 11, 13, 9]`.
- Hoogste punt: **13 meter** (bereikt in uur 9).

```python
# Start Code
veranderingen = [3, -1, 5, -2, 4, -3, 6, -1, 2, -4]
hoogte = 0
hoogtes = []

# Deel 1: bouw de hoogtes-lijst
for verandering in veranderingen:
    # Werk hoogte bij en voeg toe aan hoogtes
    pass

# Deel 2: zoek de hoogste hoogte (geen max() toegestaan!)
hoogste = 0
for h in hoogtes:
    # Als h groter is dan hoogste, werk hoogste bij
    pass

print(f"Hoogte-geschiedenis: {hoogtes}")
print(f"Hoogste punt bereikt: {hoogste} meter")
```

---

## Puzzel 5: De Stuiterende Bal (Uitdagend)
**Het Verhaal**: Een rubberbal wordt losgelaten van **100 meter**. Elke keer dat hij stuitert, bereikt hij **60%** van de vorige hoogte. Je noteert elke stuiterhoogte (afgerond op 2 decimalen) — maar alleen zolang de hoogte **≥ 1 meter** is (daaronder beweegt hij nauwelijks meer).

**De Vraag**: Bouw een `stuiters`-lijst van alle geregistreerde stuiterhoogtes. Hoeveel stuiters zijn er geregistreerd? Wat is de hoogte van de **5e stuiter**?

**Voorbeeld Test**:
- Start 10m, factor 0.5: stuiter 1 = 5.0, stuiter 2 = 2.5, stuiter 3 = 1.25, stuiter 4 = 0.625 → stop.
- Geregistreerde stuiters: `[5.0, 2.5, 1.25]`, aantal = **3**, 2e stuiter = **2.5**.

**Hint**: Start `hoogte = 100.0`. Gebruik `while True:`. Daarbinnen: werk bij `hoogte = round(hoogte * 0.6, 2)`. Als `hoogte < 1`, gebruik `break` om te stoppen. Anders, `stuiters.append(hoogte)`. Gebruik dan `stuiters[4]` voor de 5e stuiter (lijsten beginnen op index 0!).

**Controleer je Logica**:
- Stuiter 1: **60.0**, Stuiter 2: **36.0**, Stuiter 3: **21.6**, Stuiter 4: **12.96**, Stuiter 5: **7.78**.
- Totaal geregistreerde stuiters (hoogte ≥ 1): **9**.
- Stuiter 10 = 0.6 (< 1, niet geregistreerd).

```python
# Start Code
hoogte = 100.0
stuiter_factor = 0.6
stuiters = []

while True:
    hoogte = round(hoogte * stuiter_factor, 2)
    if hoogte < 1:
        break
    # Voeg hoogte toe aan stuiters
    pass

print(f"Alle stuiters: {stuiters}")
print(f"Aantal stuiters: {len(stuiters)}")
print(f"5e stuiter hoogte: {stuiters[4]}")  # index 4 = 5e item
```
