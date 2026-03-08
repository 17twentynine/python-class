# Logische Puzzels: Lijsten
Datum: 1 mrt 2026
Onderwerp: Lijsten — Opbouwen, Filteren & Zoeken

*Vijf puzzels om de lijst te leren kennen — Python's meest gebruikte container. Een lijst bewaard meerdere waarden in één variabele: `mand = []` start leeg; `mand.append(x)` voegt `x` toe aan het einde; `len(mand)` vertelt hoeveel items erin zitten. Hieronder nog vijf oefeningen (makkelijk tot moeilijk).*

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

---

## Puzzel 6: De Verzamelaar van Kwadraten (Makkelijk)
**Het Verhaal**: Je wilt een lijst van **kwadraten** van de getallen 1 tot en met 8 (1², 2², 3², …). Elk gekwadrateerd getal komt in een lijst.

**De Vraag**: Bouw een `kwadraten`-lijst met een lus. Wat is de lijst? Wat is de **som** van de kwadraten?

**Voorbeeld Test**:
- Getallen 1 tot 4: kwadraten = `[1, 4, 9, 16]`, som = **30**.

**Hint**: `kwadraten = []`, dan lus `for n in range(1, 9):` en `kwadraten.append(n * n)`.

**Controleer je Logica**:
- Lijst kwadraten: `[1, 4, 9, 16, 25, 36, 49, 64]`.
- Som van de kwadraten: **204**.

```python
# Start Code
kwadraten = []

for n in range(1, 9):
    # Voeg n² toe aan kwadraten
    pass

print(f"Kwadraten: {kwadraten}")
print(f"Som: {sum(kwadraten)}")
```

---

## Puzzel 7: De Eerste Geslaagde (Makkelijk–Gemiddeld)
**Het Verhaal**: Een leraar kijkt de examenscores in volgorde na. Ze zoekt de **eerste** score die **≥ 70** is (eerste geslaagde). Ze wil ook weten **op welke positie** (index) die score staat.

Scores: `[55, 62, 48, 71, 59, 88, 73, 65]`

**De Vraag**: Loop door de lijst. Als je de eerste score ≥ 70 vindt, bewaar die en de index, en stop. Print de waarde en de positie (bijv. "Eerste geslaagde op index 3: 71").

**Voorbeeld Test**:
- Scores `[60, 65, 72, 80]`: eerste geslaagde is **72** op index **2**.

**Hint**: Gebruik `for i in range(len(scores)):` zodat je zowel index `i` als waarde `scores[i]` hebt. Als `scores[i] >= 70`, bewaar waarde en index, dan `break`.

**Controleer je Logica**:
- Eerste score ≥ 70: **71** op index **3** (4e positie).

```python
# Start Code
scores = [55, 62, 48, 71, 59, 88, 73, 65]
eerste_geslaagd_waarde = None
eerste_geslaagd_index = None

for i in range(len(scores)):
    # Als scores[i] >= 70, zet eerste_geslaagd_waarde en eerste_geslaagd_index, dan break
    pass

print(f"Eerste geslaagde op index {eerste_geslaagd_index}: {eerste_geslaagd_waarde}")
```

---

## Puzzel 8: Het Dagelijkse Verschil (Gemiddeld)
**Het Verhaal**: Een weerstation noteert elke dag de **temperatuur om 12 uur** voor een week. Je wilt een lijst van **dag-tot-dag veranderingen**: temperatuur vandaag min gisteren.

Temperaturen: `[20, 22, 19, 23, 21, 24, 20]`

**De Vraag**: Bouw een `verschillen`-lijst. Het eerste getal is `temperaturen[1] - temperaturen[0]`, het tweede is `temperaturen[2] - temperaturen[1]`, enz. Hoeveel verschillen zijn er?

**Voorbeeld Test**:
- Temps `[10, 15, 12]` → verschillen = `[5, -3]` (twee verschillen).

**Hint**: `verschillen = []`. Lus met `for i in range(1, len(temperaturen)):` en voeg toe `temperaturen[i] - temperaturen[i - 1]`.

**Controleer je Logica**:
- Verschillen: `[2, -3, 4, -2, 3, -4]` (lengte **6**).

```python
# Start Code
temperaturen = [20, 22, 19, 23, 21, 24, 20]
verschillen = []

for i in range(1, len(temperaturen)):
    # Voeg (vandaag - gisteren) toe aan verschillen
    pass

print(f"Dag-tot-dag verschillen: {verschillen}")
print(f"Aantal verschillen: {len(verschillen)}")
```

---

## Puzzel 9: Geen Duplicaten (Gemiddeld–Moeilijk)
**Het Verhaal**: Je hebt een lijst waar getallen kunnen herhalen. Je wilt een **nieuwe** lijst waar elk getal **alleen de eerste keer** dat het voorkomt staat. De volgorde blijft hetzelfde.

Getallen: `[3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]`

**De Vraag**: Bouw een `uniek`-lijst. Loop over de originele lijst; voeg een getal alleen aan `uniek` toe als het **nog niet** in `uniek` zit.

**Voorbeeld Test**:
- `[2, 3, 2, 4, 3]` → uniek = `[2, 3, 4]`.

**Hint**: `uniek = []`. Voor elke `x in getallen:` controleer `if x not in uniek:` en dan `uniek.append(x)`.

**Controleer je Logica**:
- Unieke lijst: `[3, 1, 4, 5, 9, 2, 6]` (lengte **7**).

```python
# Start Code
getallen = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
uniek = []

for x in getallen:
    # Als x nog niet in uniek zit, voeg toe
    pass

print(f"Uniek (volgorde behouden): {uniek}")
print(f"Aantal: {len(uniek)}")
```

---

## Puzzel 10: De Som van Drie Opeenvolgende (Uitdagend)
**Het Verhaal**: Je hebt een lijst getallen. Je wilt een nieuwe lijst waar elk item de **som van drie opeenvolgende** getallen is: eerste = nums[0]+nums[1]+nums[2], tweede = nums[1]+nums[2]+nums[3], enz.

Getallen: `[10, 20, 30, 40, 50, 60]`

**De Vraag**: Bouw een `drietal_sommen`-lijst. Gebruik een lus over **indices** zodat je bij `nums[i]`, `nums[i+1]` en `nums[i+2]` kunt. Hoe ver kan `i` gaan? (Stop als er geen drie getallen meer over zijn.)

**Voorbeeld Test**:
- `[5, 10, 15, 20]` → drietal_sommen = `[30, 45]` (5+10+15 en 10+15+20).

**Hint**: Lus `for i in range(len(nums) - 2):`. Daarbinnen: voeg toe `nums[i] + nums[i+1] + nums[i+2]` aan `drietal_sommen`.

**Controleer je Logica**:
- Drietal-sommen: `[60, 90, 120, 150]` (lengte **4**).
- Eerste som = 10+20+30 = **60**, laatste = 40+50+60 = **150**.

```python
# Start Code
nums = [10, 20, 30, 40, 50, 60]
drietal_sommen = []

for i in range(len(nums) - 2):
    # Voeg som van nums[i], nums[i+1], nums[i+2] toe
    pass

print(f"Drietal-sommen: {drietal_sommen}")
print(f"Aantal: {len(drietal_sommen)}")
```
